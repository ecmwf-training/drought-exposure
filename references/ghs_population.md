# GHS Population Data

The **Global Human Settlement (GHS)** framework is developed by the European Commission's Joint Research Centre (JRC). It provides multi-temporal, global datasets on human population, settlements, and urbanisation derived from Earth Observation data and census records.

Two GHS datasets are used in this book as exposure data for drought risk assessments:

---

## GHS-POP — Population Grid (1975–2030)

**Full name**: GHS Population Grid, multitemporal (1975–2030), Release 2023  
**Coverage**: Global, 1975–2030 in 5-year intervals  
**Resolution**: 30 arc-seconds (~1 km at the equator) in WGS84 (EPSG:4326)  
**Source**: [human-settlement.emergency.copernicus.eu/ghs_pop2023.php](https://human-settlement.emergency.copernicus.eu/ghs_pop2023.php)

GHS-POP disaggregates census-based population counts into a regular raster grid using built-up surface area as a proxy for where people live. The historical time steps are grounded in census data and satellite-derived built-up layers; the 2025 and 2030 time steps are short-range projections.

**Data citation**: {cite}`schiavina2023ghspop`  
**Methodology reference**: {cite}`pesaresi2024ghsl`

---

## GHS-WUP-POP — Urban Population Projections (1975–2100)

**Full name**: GHS-WUP Population Grid, Release 2025  
**Coverage**: Global, 1975–2100 in 5-year intervals  
**Resolution**: 30 arc-seconds (~1 km at the equator) in WGS84 (EPSG:4326)  
**Source**: [human-settlement.emergency.copernicus.eu/ghs_wup_pop_r2025a.php](https://human-settlement.emergency.copernicus.eu/ghs_wup_pop_r2025a.php)

GHS-WUP-POP extends the GHS-POP historical baseline into the future using the **CRISP model** (City-Region Integrated Simulation of Population), which projects population by degree of urbanisation consistent with the UN World Urbanization Prospects. The dataset therefore reaches 2100, making it better suited for long-range climate impact analyses.

**Data citation**: {cite}`schiavina2025ghswup`  
**Model reference**: {cite}`jacobscrisioni2025crisp`

---

## Why do the two datasets differ?

Even for overlapping years (1975–2030), GHS-POP and GHS-WUP-POP can produce different population estimates for the same region. The key reasons are:

| Aspect | GHS-POP | GHS-WUP-POP |
|---|---|---|
| **Historical basis** | Census data + built-up satellite layers | GHS-POP R2023 as starting point |
| **Future projections** | Short-range (up to 2030) | Long-range via CRISP model (to 2100) |
| **Urbanisation concept** | Total population per grid cell | Population by degree of urbanisation |
| **Projection method** | Extrapolation from built-up growth | UN WUP-consistent urban/rural shares |
| **Time horizon** | 1975–2030 | 1975–2100 |

Because GHS-WUP-POP is derived from GHS-POP but then adjusted to match urban/rural population shares from the UN World Urbanization Prospects, it redistributes population spatially and may yield slightly different totals at the regional scale.

```{admonition} Which dataset to use?
:class: tip
- Use **GHS-POP** when you need historically grounded estimates up to 2030.
- Use **GHS-WUP-POP** when your analysis extends beyond 2030 or when you want projections consistent with UN urbanisation scenarios.
```
