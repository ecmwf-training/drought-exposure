"""
data4arcgis.py

Export all figures (PNG) and data (CSV) needed for the ArcGIS Story Map on
drought exposure in Central Greece (EL64).

Outputs are written to:
    arcgis_exports/png/   – 7 publication-quality PNGs (300 dpi)
    arcgis_exports/csv/   – 7 CSVs ready to upload to Datawrapper

Run from the project root:
    python data4arcgis.py
"""

import os
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# ── Configuration ──────────────────────────────────────────────────────────────
admin_id       = 'EL64'
baseline_start = 1991
baseline_end   = 2020
rolling_window = 30

workdir  = Path(__file__).resolve().parent
data_dir = workdir / 'data' / admin_id

out_root = workdir / 'arcgis_exports'
out_png  = out_root / 'png'
out_csv  = out_root / 'csv'

out_png.mkdir(parents=True, exist_ok=True)
out_csv.mkdir(parents=True, exist_ok=True)

os.chdir(workdir)

plt.rcParams.update({'font.size': 11})
DPI = 300

# ── Helper functions ───────────────────────────────────────────────────────────
def save_png(name):
    path = out_png / f'{name}.png'
    plt.savefig(path, dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"  PNG → {path.relative_to(workdir)}")


def save_csv(df, name):
    path = out_csv / f'{name}.csv'
    df.to_csv(path, index=False)
    print(f"  CSV → {path.relative_to(workdir)}")


def spines_off(ax):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)


def pop_formatter(x, pos):
    return f'{x/1e6:.2f}M' if x >= 1e6 else f'{x/1e3:.0f}K'


def proj_stats(df):
    """Multi-model median + 17th/83rd percentile of dmd by year."""
    return df.groupby('year').agg(
        dmd_median=('dmd', 'median'),
        dmd_p17   =('dmd', lambda x: np.percentile(x, 17)),
        dmd_p83   =('dmd', lambda x: np.percentile(x, 83)),
    ).reset_index()


def exposure_stats(df):
    """Multi-model median + 17th/83rd percentile of exposure by year."""
    return df.groupby('year').agg(
        exposure_median=('exposure', 'median'),
        exposure_p17   =('exposure', lambda x: np.percentile(x, 17)),
        exposure_p83   =('exposure', lambda x: np.percentile(x, 83)),
    ).reset_index()


# ── Load data ──────────────────────────────────────────────────────────────────
print("Loading data...")

drought_hist_raw = pd.read_csv(
    data_dir / 'drought_hazard' / f'drought_duration_reanalysis_{admin_id}.csv'
)
drought_hist_raw['time'] = pd.to_datetime(drought_hist_raw['time'])
drought_hist_raw['year'] = drought_hist_raw['time'].dt.year
drought_hist_raw = drought_hist_raw.sort_values('year')

drought_proj_df = pd.read_csv(
    data_dir / 'drought_hazard' / f'drought_duration_projections_{admin_id}.csv'
)
drought_proj_df['time'] = pd.to_datetime(drought_proj_df['time'])
drought_proj_df['year'] = drought_proj_df['time'].dt.year

pop_raw_wup = pd.read_csv(
    data_dir / 'ghs_population' / f'population_ghs_wup_{admin_id}.csv'
)
pop_raw_pop = pd.read_csv(
    data_dir / 'ghs_population' / f'population_ghs_pop_{admin_id}.csv'
)

# Forward-fill GHS-WUP to cover every year in the full data range
all_years = pd.DataFrame({'year': range(
    min(drought_hist_raw['year'].min(), drought_proj_df['year'].min()),
    max(drought_hist_raw['year'].max(), drought_proj_df['year'].max()) + 1,
)})
pop_df_filled = all_years.merge(pop_raw_wup, on='year', how='left')
pop_df_filled['population'] = pop_df_filled['population'].ffill()

# Historical exposure
hist_exposure = drought_hist_raw[['year', 'dmd']].merge(
    pop_df_filled, on='year', how='inner'
)
hist_exposure['exposure'] = hist_exposure['dmd'] * hist_exposure['population']

# Projection statistics (annual, no smoothing)
rcp45_df = drought_proj_df[drought_proj_df['scenario'] == 'RCP4_5'].copy()
rcp85_df = drought_proj_df[drought_proj_df['scenario'] == 'RCP8_5'].copy()

rcp45_exposure = rcp45_df.merge(pop_df_filled, on='year', how='inner')
rcp45_exposure['exposure'] = rcp45_exposure['dmd'] * rcp45_exposure['population']

rcp85_exposure = rcp85_df.merge(pop_df_filled, on='year', how='inner')
rcp85_exposure['exposure'] = rcp85_exposure['dmd'] * rcp85_exposure['population']

rcp45_stats = proj_stats(rcp45_df).merge(
    exposure_stats(rcp45_exposure), on='year'
)
rcp85_stats = proj_stats(rcp85_df).merge(
    exposure_stats(rcp85_exposure), on='year'
)

# 30-year rolling-mean projection statistics
def rolling_proj_stats(scenario, window=30):
    d = drought_proj_df[drought_proj_df['scenario'] == scenario].copy()
    d['dmd'] = d.groupby('model')['dmd'].transform(
        lambda x: x.rolling(window=window, center=True, min_periods=1).mean()
    )
    exp = d.merge(pop_df_filled, on='year', how='inner')
    exp['exposure'] = exp['dmd'] * exp['population']
    return proj_stats(d).merge(exposure_stats(exp), on='year')

rcp45_rm = rolling_proj_stats('RCP4_5')
rcp85_rm = rolling_proj_stats('RCP8_5')

# Per-model change factors for boxplot
period_order = ['Near-term', 'Mid-term', 'Long-term']
factor_periods = {
    'Near-term': (2021, 2050),
    'Mid-term' : (2041, 2070),
    'Long-term': (2071, 2100),
}

baseline_dmd_models = (
    drought_proj_df[drought_proj_df['year'].between(baseline_start, baseline_end)]
    .groupby(['model', 'scenario'])['dmd'].mean()
    .reset_index()
    .groupby('model')['dmd'].mean()
    .reset_index()
    .rename(columns={'dmd': 'baseline_dmd'})
)
baseline_pop_median = pop_df_filled[
    pop_df_filled['year'].between(baseline_start, baseline_end)
]['population'].median()

period_results = {}
for period_name, (start, end) in factor_periods.items():
    period_pop_median = pop_df_filled[
        pop_df_filled['year'].between(start, end)
    ]['population'].median()
    population_factor = np.array([period_pop_median / baseline_pop_median])
    hazard_rcp45, hazard_rcp85 = [], []
    exposure_rcp45, exposure_rcp85 = [], []
    for scenario, h_list, e_list in [
        ('RCP4_5', hazard_rcp45, exposure_rcp45),
        ('RCP8_5', hazard_rcp85, exposure_rcp85),
    ]:
        period_dmd = (
            drought_proj_df[
                drought_proj_df['year'].between(start, end) &
                (drought_proj_df['scenario'] == scenario)
            ]
            .groupby('model')['dmd'].mean()
            .reset_index()
            .rename(columns={'dmd': 'period_dmd'})
        )
        m = period_dmd.merge(baseline_dmd_models, on='model')
        m['hazard_factor']   = m['period_dmd'] / m['baseline_dmd']
        m['exposure_factor'] = (
            (m['period_dmd'] * period_pop_median) /
            (m['baseline_dmd'] * baseline_pop_median)
        )
        h_list.extend(m['hazard_factor'].values)
        e_list.extend(m['exposure_factor'].values)
    period_results[period_name] = {
        'population_factor': population_factor,
        'hazard_rcp45':      np.array(hazard_rcp45),
        'hazard_rcp85':      np.array(hazard_rcp85),
        'exposure_rcp45':    np.array(exposure_rcp45),
        'exposure_rcp85':    np.array(exposure_rcp85),
    }

print("Data loaded. Generating exports...\n")

# ── Figure 1: Observed drought duration (ERA5) ────────────────────────────────
print("[1/7] Observed drought duration...")

rm = drought_hist_raw['dmd'].rolling(window=rolling_window, center=True, min_periods=1).mean()

fig, ax = plt.subplots(figsize=(14, 5))
ax.bar(drought_hist_raw['year'], drought_hist_raw['dmd'],
       color='#888888', alpha=0.4, width=0.8, label='Annual drought duration')
ax.plot(drought_hist_raw['year'], rm,
        color='#D62828', linewidth=2.5, label=f'{rolling_window}-year rolling mean')
ax.axvspan(baseline_start, baseline_end, color='#003049', alpha=0.08,
           label=f'Baseline {baseline_start}–{baseline_end}')
spines_off(ax)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Drought duration (months/year)', fontsize=12)
ax.set_title(f'Observed Drought Duration – {admin_id} (ERA5 reanalysis)',
             fontsize=14, fontweight='bold')
ax.legend(loc='upper left', fontsize=10, frameon=True)
ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
plt.tight_layout()
save_png('01_observed_drought_duration')

csv1 = drought_hist_raw[['year', 'dmd']].rename(
    columns={'dmd': 'drought_duration_months_per_year'}
).copy()
csv1['rolling_mean_30yr'] = rm.values
save_csv(csv1, '01_observed_drought_duration')

# ── Figure 2: Population comparison 1975–2030 ─────────────────────────────────
print("[2/7] Population comparison 1975–2030...")

pop_ghs_cut = pop_raw_pop[pop_raw_pop['year'] <= 2030]
pop_wup_cut = pop_raw_wup[pop_raw_wup['year'] <= 2030]

fig, ax = plt.subplots(figsize=(14, 5))
ax.plot(pop_ghs_cut['year'], pop_ghs_cut['population'],
        marker='o', linewidth=2, markersize=7, color='#2E86AB',
        label='GHS-POP (total population, 1975–2030)')
ax.plot(pop_wup_cut['year'], pop_wup_cut['population'],
        marker='s', linewidth=2, markersize=6, alpha=0.85, color='#A23B72',
        label='GHS-WUP (urban population, 1975–2030)')
ax.axvline(2020, color='gray', linestyle=':', linewidth=1.5, alpha=0.7,
           label='2020')
spines_off(ax)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Population', fontsize=12)
ax.set_title(f'Population Change in {admin_id} – Dataset Comparison (1975–2030)',
             fontsize=14, fontweight='bold')
ax.yaxis.set_major_formatter(FuncFormatter(pop_formatter))
ax.legend(fontsize=10, frameon=True)
ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
plt.tight_layout()
save_png('02_population_comparison_1975_2030')

csv2 = (
    pop_ghs_cut[['year', 'population']].rename(columns={'population': 'ghs_pop'})
    .merge(
        pop_wup_cut[['year', 'population']].rename(columns={'population': 'ghs_wup'}),
        on='year', how='outer'
    )
    .sort_values('year')
)
save_csv(csv2, '02_population_comparison_1975_2030')

# ── Figure 3: Population projection to 2100 ───────────────────────────────────
print("[3/7] Population projection to 2100...")

fig, ax = plt.subplots(figsize=(14, 5))
ax.plot(pop_raw_wup['year'], pop_raw_wup['population'],
        linewidth=2.5, color='#A23B72',
        label='GHS-WUP projection (1975–2100)')
ax.axvline(2020, color='gray', linestyle=':', linewidth=1.5, alpha=0.7,
           label='2020')
ax.axvspan(baseline_start, baseline_end, color='#003049', alpha=0.08,
           label=f'Baseline {baseline_start}–{baseline_end}')
spines_off(ax)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Population', fontsize=12)
ax.set_title(f'Population Projection – {admin_id} (GHS-WUP, 1975–2100)',
             fontsize=14, fontweight='bold')
ax.yaxis.set_major_formatter(FuncFormatter(pop_formatter))
ax.legend(fontsize=10, frameon=True)
ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
plt.tight_layout()
save_png('03_population_projection_to_2100')

save_csv(pop_raw_wup[['year', 'population']].copy(),
         '03_population_projection_to_2100')

# ── Figure 4: Historical exposure components (3-panel) ────────────────────────
print("[4/7] Historical exposure components...")

fig, axes = plt.subplots(3, 1, figsize=(14, 11), sharex=True)

axes[0].bar(hist_exposure['year'], hist_exposure['dmd'],
            color='#D62828', alpha=0.55, width=0.8)
axes[0].set_ylabel('Drought duration\n(months/year)', fontsize=11)
axes[0].set_title(
    f'Historical Drought Exposure Components – Central Greece ({admin_id})',
    fontsize=14, fontweight='bold', pad=15
)
spines_off(axes[0])
axes[0].grid(True, alpha=0.3, linestyle='--', linewidth=0.5)

axes[1].plot(hist_exposure['year'], hist_exposure['population'] / 1e6,
             color='#003049', linewidth=2)
axes[1].set_ylabel('Population\n(millions)', fontsize=11)
spines_off(axes[1])
axes[1].grid(True, alpha=0.3, linestyle='--', linewidth=0.5)

axes[2].fill_between(hist_exposure['year'], 0, hist_exposure['exposure'] / 1e6,
                     color='#F77F00', alpha=0.6)
axes[2].plot(hist_exposure['year'], hist_exposure['exposure'] / 1e6,
             color='#F77F00', linewidth=2)
axes[2].set_ylabel('Drought exposure\n(million person-months/year)', fontsize=11)
axes[2].set_xlabel('Year', fontsize=12)
spines_off(axes[2])
axes[2].grid(True, alpha=0.3, linestyle='--', linewidth=0.5)

for ax in axes:
    ax.axvspan(baseline_start, baseline_end, color='gray', alpha=0.08)

plt.tight_layout()
save_png('04_historical_exposure_components')

csv4 = hist_exposure[['year', 'dmd', 'population', 'exposure']].rename(columns={
    'dmd':      'drought_duration_months_per_year',
    'exposure': 'exposure_person_months_per_year',
})
save_csv(csv4, '04_historical_exposure')

# ── Figure 5: Future drought duration — 30-year rolling mean ──────────────────
print("[5/7] Projected drought duration (30yr rolling mean)...")

fig, ax = plt.subplots(figsize=(14, 6))

ax.plot(drought_hist_raw['year'], rm,
        color='black', linewidth=2.5, label='Observed (ERA5, 30yr mean)', zorder=5)

ax.fill_between(rcp45_rm['year'], rcp45_rm['dmd_p17'], rcp45_rm['dmd_p83'],
                color='#F77F00', alpha=0.2)
ax.plot(rcp45_rm['year'], rcp45_rm['dmd_median'],
        color='#F77F00', linewidth=2.5,
        label='RCP4.5 – multi-model median (30yr mean)')

ax.fill_between(rcp85_rm['year'], rcp85_rm['dmd_p17'], rcp85_rm['dmd_p83'],
                color='#D62828', alpha=0.2)
ax.plot(rcp85_rm['year'], rcp85_rm['dmd_median'],
        color='#D62828', linewidth=2.5,
        label='RCP8.5 – multi-model median (30yr mean)')

ax.axvspan(baseline_start, baseline_end, color='gray', alpha=0.1,
           label=f'Baseline {baseline_start}–{baseline_end}')
spines_off(ax)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Drought duration (months/year)', fontsize=12)
ax.set_title(f'Projected Drought Duration – {admin_id} (30-year rolling mean)',
             fontsize=14, fontweight='bold')
ax.legend(fontsize=10, frameon=True)
ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
plt.tight_layout()
save_png('05_projected_drought_duration')

csv5 = (
    rcp45_rm[['year', 'dmd_median', 'dmd_p17', 'dmd_p83']].rename(columns={
        'dmd_median': 'rcp45_median', 'dmd_p17': 'rcp45_p17', 'dmd_p83': 'rcp45_p83'
    })
    .merge(
        rcp85_rm[['year', 'dmd_median', 'dmd_p17', 'dmd_p83']].rename(columns={
            'dmd_median': 'rcp85_median', 'dmd_p17': 'rcp85_p17', 'dmd_p83': 'rcp85_p83'
        }),
        on='year', how='outer'
    )
    .sort_values('year')
)
save_csv(csv5, '05_projected_drought_duration')

# ── Figure 6: Combined future exposure — historical + both RCPs ───────────────
print("[6/7] Combined future exposure timeseries...")

fig, ax = plt.subplots(figsize=(14, 6))

ax.plot(hist_exposure['year'], hist_exposure['exposure'] / 1e6,
        color='black', linewidth=2.5,
        label='Historical (ERA5 + GHS-WUP)', alpha=0.9, zorder=5)

ax.fill_between(rcp45_stats['year'],
                rcp45_stats['exposure_p17'] / 1e6,
                rcp45_stats['exposure_p83'] / 1e6,
                color='#F77F00', alpha=0.2)
ax.plot(rcp45_stats['year'], rcp45_stats['exposure_median'] / 1e6,
        color='#F77F00', linewidth=2.5, label='RCP4.5 – multi-model median')

ax.fill_between(rcp85_stats['year'],
                rcp85_stats['exposure_p17'] / 1e6,
                rcp85_stats['exposure_p83'] / 1e6,
                color='#D62828', alpha=0.2)
ax.plot(rcp85_stats['year'], rcp85_stats['exposure_median'] / 1e6,
        color='#D62828', linewidth=2.5, label='RCP8.5 – multi-model median')

ax.axvspan(baseline_start, baseline_end, color='gray', alpha=0.1,
           label=f'Baseline {baseline_start}–{baseline_end}')
ax.axvline(2005, color='gray', linestyle=':', linewidth=1.5, alpha=0.6)
spines_off(ax)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Drought exposure\n(million person-months/year)', fontsize=12)
ax.set_title(f'Drought Exposure: Historical and Projected – {admin_id}',
             fontsize=14, fontweight='bold')
ax.legend(fontsize=10, frameon=True)
ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
plt.tight_layout()
save_png('06_future_exposure_combined')

csv6 = (
    rcp45_stats[['year', 'exposure_median', 'exposure_p17', 'exposure_p83']].rename(columns={
        'exposure_median': 'rcp45_median',
        'exposure_p17':    'rcp45_p17',
        'exposure_p83':    'rcp45_p83',
    })
    .merge(
        rcp85_stats[['year', 'exposure_median', 'exposure_p17', 'exposure_p83']].rename(columns={
            'exposure_median': 'rcp85_median',
            'exposure_p17':    'rcp85_p17',
            'exposure_p83':    'rcp85_p83',
        }),
        on='year', how='outer'
    )
    .merge(
        hist_exposure[['year', 'exposure']].rename(columns={'exposure': 'historical'}),
        on='year', how='outer'
    )
    .sort_values('year')
)
save_csv(csv6, '06_future_exposure_combined')

# ── Figure 7: Boxplot — near/mid/long-term change factors ─────────────────────
print("[7/7] Boxplot near/mid/long-term factors...")

data_to_plot = []
box_colors   = []
for period_name in period_order:
    res = period_results[period_name]
    data_to_plot.extend([
        res['population_factor'],
        res['hazard_rcp45'],
        res['hazard_rcp85'],
        res['exposure_rcp45'],
        res['exposure_rcp85'],
    ])
    box_colors.extend(['#003049', '#F77F00', '#D62828', '#F77F00', '#D62828'])

x_positions = [
    1.1, 1.2, 1.3, 1.4, 1.5,
    2.1, 2.2, 2.3, 2.4, 2.5,
    3.1, 3.2, 3.3, 3.4, 3.5,
]

fig, ax = plt.subplots(figsize=(14, 6))

for x_start in [1.35, 2.35, 3.35]:
    ax.add_patch(plt.Rectangle(
        (x_start, -1), 0.2, 5, facecolor='grey', alpha=0.2
    ))

bp = ax.boxplot(
    data_to_plot,
    patch_artist=True,
    widths=0.075,
    showfliers=False,
    positions=x_positions,
    tick_labels=None,
    boxprops=dict(linewidth=1.0),
    medianprops=dict(color='black', linewidth=1.0),
    whiskerprops=dict(linewidth=1.0),
    capprops=dict(linewidth=1.0),
)

for ii, (patch, color) in enumerate(zip(bp['boxes'], box_colors)):
    patch.set_facecolor(color)
    patch.set_edgecolor(color)
    patch.set_alpha(1.0 if ii % 5 in [3, 4] else 0.5)

ax.axhline(1.0, color='gray', linestyle='--', linewidth=1.5, alpha=0.7)
ax.set_xlim(0.9, 3.8)
ax.set_ylim(0, max(max(d) for d in data_to_plot) * 1.15)
ax.set_xticks([])

y_bottom = ax.get_ylim()[0]
y_label_y = y_bottom - 0.12 * (ax.get_ylim()[1] - y_bottom)
period_x = {'Near-term': 1.3, 'Mid-term': 2.3, 'Long-term': 3.3}
period_labels = {
    'Near-term': 'Near-term\n(2021–2050)',
    'Mid-term':  'Mid-term\n(2041–2070)',
    'Long-term': 'Long-term\n(2071–2100)',
}
for p, x in period_x.items():
    ax.text(x, y_label_y, period_labels[p], ha='center', va='top', fontsize=11)

legend_elements = [
    plt.Line2D([0], [0], color='#003049', lw=5, alpha=1,   label='Population'),
    plt.Line2D([0], [0], color='#F77F00', lw=5, alpha=0.5, label='Hazard – RCP4.5'),
    plt.Line2D([0], [0], color='#D62828', lw=5, alpha=0.5, label='Hazard – RCP8.5'),
    plt.Line2D([0], [0], color='#F77F00', lw=5, alpha=1,   label='Exposure – RCP4.5'),
    plt.Line2D([0], [0], color='#D62828', lw=5, alpha=1,   label='Exposure – RCP8.5'),
]
ax.legend(handles=legend_elements, loc='upper left', fontsize=10, frameon=True)
ax.set_ylabel('Change relative to 1991–2020 baseline [factor]', fontsize=12)
ax.set_title(
    f'Projected Changes in Population, Hazard, and Exposure\nCentral Greece ({admin_id})',
    fontsize=14, fontweight='bold',
)
spines_off(ax)
ax.grid(True, axis='y', alpha=0.3, linestyle='--', linewidth=0.5)
plt.tight_layout()
save_png('07_boxplot_near_mid_longterm')

rows = []
for period_name in period_order:
    res = period_results[period_name]
    for var_name, values in res.items():
        rows.append({
            'period':   period_name,
            'variable': var_name,
            'median':   float(np.median(values)),
            'p17':      float(np.percentile(values, 17)),
            'p83':      float(np.percentile(values, 83)),
            'min':      float(np.min(values)),
            'max':      float(np.max(values)),
            'n':        len(values),
        })
save_csv(pd.DataFrame(rows), '07_boxplot_factors')

# ── Summary ────────────────────────────────────────────────────────────────────
print(f"""
Done. All outputs are in:

  arcgis_exports/png/
    01_observed_drought_duration.png
    02_population_comparison_1975_2030.png
    03_population_projection_to_2100.png
    04_historical_exposure_components.png
    05_projected_drought_duration.png
    06_future_exposure_combined.png
    07_boxplot_near_mid_longterm.png

  arcgis_exports/csv/
    01_observed_drought_duration.csv
    02_population_comparison_1975_2030.csv
    03_population_projection_to_2100.csv
    04_historical_exposure.csv
    05_projected_drought_duration.csv
    06_future_exposure_combined.csv
    07_boxplot_factors.csv
""")
