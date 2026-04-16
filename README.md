# Towards Drought-Resilient Regions

This is a Jupyter Book providing hands-on tools and explanations to help European regions and municipalities estimate past and future drought impact on people and agriculture. It has been developed in the context of the VALORADA project to support the use of climate data; specifically the promotion of 'good practice' and showcase how open-source data can be used to support regional climate risk and vulnerability assessments.

## Overview

This resource supports local decision-makers and analysts in assessing **drought hazard, exposure, and risk** using open climate and population data. The notebooks follow the (diataxis framework)[https://diataxis.fr], which is a systematic, user-centric approach to technical documentation. Following this framework, documentation is categorized into four distinct types based on the user's needs --- tutorials, how-to guides,  references, and explanation --- rather than just the structure of the software. This approach allows VALORADA to support intermediaries access climate data from the Copernicus Climate Change Service (C3S) and showcase how the approach can be made scalable to other regions and climate hazards. The categories comprise:

- **Tutorials** — end-to-end storylines (e.g. changing drought duration, population and agricultural exposure to prolonged droughts)
- **How-to guides** — step-by-step instructions for acquiring and processing input datasets (climate hazard, population, land cover, regional boundaries)
- **Explanations** — background on drought science, risk frameworks (hazard × exposure × vulnerability)
- **References** — technical references and background information

## Data Sources

| Type | Dataset |
|------|---------|
| Drought hazard | [European Climate Data Explorer (ECDE)](https://climate.copernicus.eu/ecde) — ERA5 reanalysis (1940–2023) and Euro-COR projections (RCP 4.5 & 8.5, to 2100) |
| Population | GHS-POP and GHS-WUP-POP (EU Global Human Settlement Layer) |
| Land cover | CORINE Land Cover and satellite-derived land cover |
| Regions | NUTS2 shapefiles (Eurostat, 2024) |

## Getting Started

The notebooks can be run directly in the browser — no local installation needed:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/)

To run locally, create the conda environment:

```bash
conda env create -f environment.yml
conda activate drought_exposure
```

## Repository Structure

```
tutorials/          # Storyline notebooks
how-to-guides/      # Data acquisition and processing guides
explanation/        # Background science and methodology
references/         # Project and data references
data/               # Input data (not everything is tracked in git, see how-to-guides to create all data)
```

## Funding

This work was produced in the context of the **VALORADA** project (*Validated Local Risk Actionable Data for Adaptation*), funded by the European Union under **Horizon Europe Grant Agreement No. 101112837**. VALORADA supports the EU Adaptation Mission to help 150 regions and communities become climate-resilient by 2030.

The tools are developed at the **Copernicus Climate Change Service (C3S)**, operated by ECMWF.

## License

[Apache 2.0](LICENSE)