# ArcGIS Story Map – Draft Script
**Title:** Drought Exposure in Central Greece: How Climate Change and Population Shifts Shape Future Risk  
**Subtitle:** A look at Central Greece (EL64) from 1975 to 2100  
**Format:** Guided Map Tour (sidecar layout — map on left, narrative panel on right)

---

## IMPLEMENTATION NOTES (before you start)

**What you need in ArcGIS Online:**
- Upload the NUTS2 shapefile (`data/regions/NUTS_RG_20M_2024_4326/`) as a hosted feature layer
- Create two web maps: one showing all Greek NUTS2 regions (coloured neutrally), one highlighting only EL64
- For the choropleth future panels: join the per-period exposure summary statistics to the EL64 polygon (or use a manually styled single-feature layer)

**Charts:**
- Export the four timeseries figures from the notebooks as PNGs for the draft
- For the live version: recreate them in **Datawrapper** (upload CSVs, style to match) and embed via iframe in Story Maps media blocks
- Datawrapper supports line + area charts with uncertainty bands — suitable for all four timeseries

**Story Maps block types used:** Cover → Sidecar (map tour) → Immersive panels → Image/chart embeds → Credits

---

## COVER

**Background image:** Satellite view or landscape photo of Central Greece / Thessaly plain (arid summer scene works well)

**Title:** Drought Exposure in Central Greece

**Subtitle:**  
How observed warming, shifting drought patterns, and population change combine to alter the drought risk faced by hundreds of thousands of people — from the 1970s through to the end of the century.

---

## SECTION 1 — Setting the Scene: Where is Central Greece?

**Block type:** Sidecar, Map panel left  
**Map:** All Greek NUTS2 regions, neutral fill, EL64 highlighted in orange (`#F77F00`), labelled "Central Greece (EL64)"  
**Map behaviour:** Start zoomed to Greece (zoom ~6), pan and zoom to EL64 on scroll

**Narrative panel (right):**

> Greece is divided into 13 NUTS2 administrative regions — statistical units used across Europe to monitor regional development and climatic conditions. This story focuses on **Central Greece (EL64)**, a predominantly rural region covering Thessaly, Sterea Ellada, and the surrounding mountains and coastline.
>
> Central Greece sits in one of Europe's most drought-prone zones — the Eastern Mediterranean. The region has a long record of hot, dry summers and is home to a significant agricultural sector that depends on reliable rainfall and snowmelt.
>
> But how has drought evolved here over the past 50 years, and what does climate change mean for the people who live and work in this region?

---

## SECTION 2 — The Hazard: How Has Drought Duration Changed?

**Block type:** Sidecar, chart panel left (or full-width image)  
**Chart:** `Observed Drought Duration - EL64 (ERA5 reanalysis)` from `changing_drought_duration.ipynb`  
- X-axis: Year (1950–2023)  
- Y-axis: Drought duration (months/year)  
- Annual series in black, 30-year rolling mean overlay  
- Baseline period 1991–2020 shaded  
**Datawrapper type:** Line chart with reference band

**Narrative panel:**

> Using ERA5 — a global reanalysis dataset that combines historical observations with a weather model to reconstruct past climate — we can trace how long droughts have lasted in Central Greece each year since the mid-20th century.
>
> **What the data shows:**  
> There is substantial year-to-year variability, but the 30-year rolling mean reveals a clear upward trend: drought months per year have increased since the 1980s. The 1990s and 2000s saw several particularly severe years.
>
> The **1991–2020 WMO reference period** (shaded) forms the baseline against which all future projections in this story are compared. On average, Central Greece experienced roughly **2–3 months of drought per year** during this baseline.

---

## SECTION 3 — The Exposure Factor: How Has the Population Changed?

**Block type:** Sidecar, chart panel left  
**Chart:** `Population Change in EL64 - Dataset Comparison` from `population.ipynb`, **cut to 1975–2030**  
- Show only the historical GHS-POP series and the near-term GHS-WUP extension  
- Y-axis: Population (thousands)  
- Two series: GHS-POP (solid) and GHS-WUP (dashed, for overlap period)  
**Datawrapper type:** Line chart, dual series, with a 2030 cutoff

**Narrative panel:**

> Drought hazard alone doesn't determine risk — the number of people exposed matters equally. In Central Greece, the population story is striking.
>
> Since its peak in the late 1970s, the region has seen sustained **population decline**, driven by rural-to-urban migration and an ageing demographic. By 2020, the population had fallen to roughly **half its post-war peak**.
>
> This means that even if drought duration remained constant, the number of people exposed would change simply because of demographic shifts. Understanding drought **exposure** requires tracking both variables together.

---

## SECTION 4 — Combining Hazard and Population: Historical Drought Exposure

**Block type:** Sidecar, chart panel left  
**Chart:** Historical drought exposure from `people_exposed_to_prolonged_droughts.ipynb` — Part 1 (three-panel figure or the combined exposure panel only)  
- Bottom panel only: `Drought exposure (million person-months/year)` as filled area  
- Years: 1975–2020  
**Datawrapper type:** Area chart

**Narrative panel:**

> **Exposure = Hazard × Population.**
>
> When we multiply annual drought duration (months/year) by the number of people in the region, we get a measure of total **drought exposure**: the cumulative number of person-months per year that the population collectively experiences under drought conditions.
>
> The result shows two competing forces:
> - **Increasing drought duration** (hazard) pushes exposure up
> - **Falling population** pushes exposure down
>
> During the most severe drought years on record, both factors combined to produce exposure peaks exceeding several million person-months per year. The overall trend reflects the complex interaction between a worsening climate hazard and a shrinking resident population.

---

## SECTION 5 — Into the Future: How Will Drought Duration Change?

**Block type:** Full-width immersive panel, chart embed  
**Chart:** Projected drought duration timeseries from `people_exposed_to_prolonged_droughts.ipynb` — the 30-year rolling mean comparison panel  
- Both RCP4.5 (orange) and RCP8.5 (red) multi-model medians + uncertainty bands  
- Historical reanalysis in black for continuity  
- X-axis: 1975–2100  
**Datawrapper type:** Multi-series line + area (confidence interval) chart

**Narrative panel:**

> Climate projections for Central Greece tell a consistent story across climate models: **droughts will become longer and more frequent** under both moderate (RCP4.5) and high (RCP8.5) emission scenarios.
>
> By the second half of this century:
> - Under **RCP4.5** (if strong climate action is taken), drought duration is projected to increase by roughly **2 additional months per year** relative to the 1991–2020 baseline
> - Under **RCP8.5** (if emissions continue rising), the increase approaches **2.5–3 months per year**
>
> The shaded uncertainty bands show the spread across multiple climate models — while the exact magnitude is uncertain, the direction is not: **all models agree drought duration will increase**.

---

## SECTION 6 — Into the Future: Population Projections to 2100

**Block type:** Sidecar, chart panel left  
**Chart:** Same population figure as Section 3, but now **extended to 2100** showing the full GHS-WUP projection  
- GHS-WUP only (1975–2100)  
- Mark 2020 with a vertical line ("today")  
**Datawrapper type:** Line chart with reference line

**Narrative panel:**

> The GHS-WUP dataset (Global Human Settlement — World Urbanisation Prospects) extends population projections to 2100 based on UN demographic scenarios.
>
> For Central Greece, the demographic outlook is sobering: the region's population is projected to **continue declining** throughout the 21st century. By 2100, the population could fall to just a fraction of today's level.
>
> This means future drought exposure will be shaped by **two diverging forces**: increasing drought duration pushing exposure up, and population decline pulling it down. Which force wins — and by how much — depends on the emissions pathway we follow.

---

## SECTION 7 — Future Drought Exposure Under Climate Change

**Block type:** Full-width immersive panel, chart embed  
**Chart:** Combined future exposure timeseries from `people_exposed_to_prolonged_droughts.ipynb`  
- Historical black line (ERA5 + GHS-WUP) continued into future  
- RCP4.5 multi-model median (orange) + uncertainty band  
- RCP8.5 multi-model median (red) + uncertainty band  
- Mark 1991–2020 baseline as grey shaded zone  
**Datawrapper type:** Multi-series line + area chart

**Narrative panel:**

> Combining projected drought duration with population projections gives us future **drought exposure**.
>
> Despite population decline, the increasing intensity of drought under climate change means that **exposure is projected to rise** in both scenarios. The reason: drought duration increases faster than population falls.
>
> Crucially, the spread between RCP4.5 and RCP8.5 widens sharply after 2060. **The emissions choices made in the next decade will have a large influence on how many person-months of drought exposure Central Greece faces by the end of the century.**

---

## SECTION 8 — Near-, Mid-, and Long-Term Changes at a Glance

**Block type:** Full-width media block (image) or sidecar with static chart  
**Chart:** The boxplot figure from `people_exposed_to_prolonged_droughts.ipynb` — "Projected changes in population, hazard, and exposure — Central Greece (EL64)"  
- Three time horizons: Near-term (2021–2050), Mid-term (2041–2070), Long-term (2071–2100)  
- Five boxes per horizon: Population · Hazard RCP4.5 · Hazard RCP8.5 · Exposure RCP4.5 · Exposure RCP8.5  
- Reference line at 1.0 (= no change from baseline)

**Narrative panel:**

> Bringing it all together: this chart summarises **how much each component changes** relative to the 1991–2020 baseline, expressed as a factor (1.0 = no change, 2.0 = doubled).
>
> Key messages:
> - **Population** (dark blue): steadily declines to below the baseline across all periods — a dampening effect on exposure
> - **Hazard** (lighter boxes): both RCP4.5 and RCP8.5 show drought duration increasing above the baseline, with RCP8.5 increasing more steeply in the long term
> - **Exposure** (brighter boxes): the net result — despite population decline, **exposure increases** in the long-term under both scenarios, because hazard increase outweighs population decrease
>
> The boxes show the spread across the climate model ensemble. By the long term (2071–2100), nearly all models agree on an **increase in drought exposure under RCP8.5**.

---

## CLOSING PANEL

**Block type:** Credits / narrative close

> **What this means for Central Greece**
>
> Central Greece already faces significant drought pressure. Climate change will intensify this — not because population is growing, but because droughts will become so much longer and more severe that the per-person burden increases substantially.
>
> Early climate action (the difference between RCP4.5 and RCP8.5) can meaningfully reduce these projections. At the same time, this analysis only captures **exposure** — the next step in a full risk assessment would incorporate **vulnerability** (who is most affected and why?) and **adaptation** (what measures can reduce risk?).
>
> **Data sources and methods**  
> Explore the full methodology in the accompanying JupyterBook:
> - Drought hazard: ERA5 reanalysis + CMIP5 projections via the European Climate Data Explorer (ECDE)
> - Population: GHS-POP and GHS-WUP (EU Joint Research Centre / UN World Urbanisation Prospects)
> - Region: NUTS2 EL64 (Eurostat, 2024 boundaries)

---

## CHAPTER SUMMARY TABLE

| # | Section | Map/Chart | Block type |
|---|---------|-----------|------------|
| 1 | Setting the scene | NUTS2 map of Greece, EL64 highlighted | Sidecar map |
| 2 | Historical hazard | Observed drought duration timeseries (ERA5) | Sidecar chart |
| 3 | Historical population | Population 1975–2030 (GHS-POP + GHS-WUP) | Sidecar chart |
| 4 | Historical exposure | Exposure 1975–2020 (area chart) | Sidecar chart |
| 5 | Future hazard | Projected drought duration 1975–2100, both RCPs | Immersive chart |
| 6 | Future population | Population projection to 2100 (GHS-WUP) | Sidecar chart |
| 7 | Future exposure | Projected exposure timeseries to 2100 | Immersive chart |
| 8 | Summary | Boxplot: population/hazard/exposure factors | Full-width image |
| — | Close | Credits, links to JupyterBook | Narrative |
