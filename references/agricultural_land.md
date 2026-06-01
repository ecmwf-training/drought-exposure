# Agricultural Land Cover Data

Two land cover datasets are used in this book as exposure data for agricultural drought risk assessments:

---

## CORINE Land Cover (CLC)

**Full name**: CORINE Land Cover — Coordination of Information on the Environment  
**Coverage**: Europe, time steps 1990, 2000, 2006, 2012, and 2018  
**Resolution**: 100 m in EPSG:3035 (LAEA Europe)  
**Source**: [land.copernicus.eu/en/products/corine-land-cover](https://land.copernicus.eu/en/products/corine-land-cover)

CORINE Land Cover is coordinated by the European Environment Agency (EEA) as part of the Copernicus Land Monitoring Service (CLMS). It provides a harmonised, pan-European land cover and land use inventory in 44 thematic classes arranged in a three-level nomenclature. The five available time steps (1990–2018) allow analysis of land cover change at decadal resolution across Europe. Agricultural classes include arable land, permanently irrigated land, vineyards, olive groves, pastures, and mixed cultivation patterns, among others.

**Data citation**: {cite}`eea2018corine`

---

## Satellite-based Land Cover (CDS)

**Full name**: Land cover classification gridded maps from 1992 to present derived from satellite observations  
**Coverage**: Global, 1992–present (annual)  
**Resolution**: 300 m in WGS84 (EPSG:4326)  
**Source**: [cds.climate.copernicus.eu/datasets/satellite-land-cover](https://cds.climate.copernicus.eu/datasets/satellite-land-cover)

This dataset is produced by the ESA Climate Change Initiative (ESA CCI) Land Cover project and distributed through the Copernicus Climate Data Store (CDS). It classifies land surface into 38 classes using the UN Land Cover Classification System (LCCS). Annual coverage from 1992 onward makes it well suited for continuous time-series analysis of land use change. Two product versions are used: **v2.0.7cds** (1992–2015) and **v2.1.1** (2016–present).

**Data citation**: {cite}`c3s2017satellite_landcover`

---

## How do the two datasets compare?

Both datasets capture agricultural land cover, but differ in geographic scope, temporal resolution, and thematic detail:

| Aspect | CORINE Land Cover | Satellite Land Cover |
|---|---|---|
| **Geographic scope** | Europe only | Global |
| **Time steps** | 5 snapshots (1990–2018) | Annual (1992–present) |
| **Spatial resolution** | 100 m | 300 m |
| **Classification depth** | 44 classes, 3 levels | 38 LCCS classes |
| **Update frequency** | Every 6 years | Annual |
| **Data provider** | EEA / Copernicus Land | ESA CCI / Copernicus CDS |

```{admonition} Which dataset to use?
:class: tip
- Use **CORINE Land Cover** when you need a detailed, Europe-focused classification with a rich thematic legend and a decades-long record at decadal resolution.
- Use **Satellite Land Cover** when you need annual time series, global coverage, or a longer record going back to 1992.
```
