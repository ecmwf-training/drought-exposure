# European Climate Data Explorer (ECDE)

The **European Climate Data Explorer (ECDE)** is a web application developed by the Copernicus Climate Change Service (C3S) that allows users to explore past trends and projected future changes for a range of key climate indicators from multiple datasets. Check out the application [here](https://apps.copernicus-climate.eu/c3s-apps/ecde/).

The underlying data are available through the Copernicus Climate Data Store (CDS):

**Data citation**: {cite}`c3s2024ecde`

---

## Purpose & development

The development of the ECDE was driven by the European Environment Agency (EEA) to address information needs regarding climate impact indicators relevant to national climate change adaptation initiatives across the EU. The list of indicators is based on a technical report from the European Topic Centre on Climate Change Impacts, Vulnerability and Adaptation (ETC‑CCA).

The indicators describe how climate variability and change of essential climate variables can impact sectors such as health, agriculture, forestry, energy, tourism, and water/coastal management.

---

## Data sources

**Reanalysis**: ERA5 (1940–present), the ECMWF global atmospheric reanalysis, provides a consistent historical baseline.

**Climate projections**: An ensemble of downscaled Euro-CORDEX regional climate models forced by two emissions scenarios:

| Scenario | Description |
|---|---|
| **RCP 4.5** | Intermediate emissions pathway, stabilisation around 2100 |
| **RCP 8.5** | High emissions pathway, continued rise through 2100 |

Full technical documentation: [confluence.ecmwf.int — Input data underpinning the ECDE](https://confluence.ecmwf.int/display/CKB/Input+data+underpinning+the+European+Climate+Data+Explorer%3A+Description+of+the+datasets+and+variables)

---

## Drought variable used in this book

### Duration of meteorological droughts (`dmd`)

**CDS variable name**: `duration_of_meteorological_droughts`  
**Short name**: `dmd`  
**Unit**: months per year  
**Coverage**: Europe (NUTS2 regions), 1940–2100  
**Source**: [sis-ecde-climate-indicators on CDS](https://cds.climate.copernicus.eu/datasets/sis-ecde-climate-indicators)

The **Duration of meteorological droughts** indicator counts the total number of months per year in which the Standardized Precipitation Index at the 3-month timescale (SPI-3, read more about these indices [here](../explanation/what_is_drought.md)) falls below −1, indicating a meteorological drought. It captures how many months of a year are affected by anomalously low precipitation relative to the local climatology. 

- **Reanalysis data** (ERA5): covers 1940–2023, providing an observed baseline.
- **Climate projections** (Euro-CORDEX): cover 1950–2100 for an ensemble of GCM–RCM combinations under RCP 4.5 and RCP 8.5.

```{admonition} Interpreting the indicator
:class: note
A value of 3 months/year means that, in that year, SPI-3 dropped below −1 during three separate months. Higher values indicate more widespread or persistent drought conditions. Trends in this indicator over time reflect changes in both drought frequency and duration under climate change.
```

