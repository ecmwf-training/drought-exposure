# What is a drought?

Drought is a complex phenomenon — it develops slowly, varies across regions, and affects different parts of the water cycle in different ways.  
To understand what drought is, we need to understand the types of drought, and how drought **indices** help to quantify drought and why they matter.

This page gives a short overview of the broader drought types (meteorological, agricultural, hydrological) and then focuses on two of the most widely used climate-based drought indicators: **SPI** and **SPEI**.  

For deeper reading, we link to authoritative sources such as the **World Meteorological Organization (WMO)**, the **European Drought Observatory (EDO)**, and the **Global Drought Observatory (GDO)**.

---

## Types of drought: meteorological, agricultural, and hydrological

Drought is not a single concept, as drought moves across different parts of the water cycle.  
Understanding the major drought types helps interpret what drought indices can (and cannot) capture.

![Image](../img/drought_types.png "Types of drought")

---

### Meteorological drought

**Definition:**  
A period of significantly below-normal precipitation (Gibbs & Maher, 1967).

**Where it occurs:**  
In the **atmosphere** — expressed in rainfall anomalies.

**Indicators:**  
- Percentiles  
- Standardized Precipitation Index (SPI)
- Standardized Precipitation Evapotranspiration Index (SPEI)

**Timescale:** Weeks to months  
**Significance:** First stage of drought development.

---

### Agricultural (soil moisture) drought

**Definition:**  
Insufficient soil moisture to meet vegetation or crop needs (FAO, 2013).

**Where it occurs:**  
**Root zone and surface soils**

**Indicators:**  
- Soil moisture anomalies  
- Evaporative Stress Index (ESI)  
- NDVI/vegetation indices  
- SPEI (via temperature sensitivity)

**Timescale:** Weeks to months  
**Impacts:** Crop failures, vegetation stress, fire risk.

---

### Hydrological drought

**Definition:**  
Long-term deficits in **streamflow, groundwater, lakes, or reservoirs** (Van Loon, 2015).

**Where it occurs:**  
The **deep water cycle**

**Indicators:**  
- River discharge  
- Groundwater levels  
- Reservoir storage  

**Timescale:** Months to years  
**Impacts:** Water supply, navigation, hydropower, ecosystems.

---

### How drought types relate

Meteorological drought is often the **starting point** of drought development, and many drought events progress from **meteorological → agricultural → hydrological** stages. However, this sequence is **not guaranteed**, and real-world drought propagation is more complex:

- **Heatwaves** can trigger agricultural drought even when rainfall is near normal  
- **Irrigation** or groundwater pumping can temporarily buffer agricultural drought  
- **Hydrological drought** can persist long after rainfall recovers  
- **Soil characteristics, land use, and snowpack dynamics** can accelerate or delay the transition  

Because of this complexity, the **timescale** over which precipitation deficits accumulate becomes a key factor. Longer deficits generally translate into deeper and more persistent impacts across the water cycle.

A simplified view:

- **Short-term deficits (1 month / SPI-1 or SPEI-1)**  
  → Reduced soil moisture, stress on vegetation, and lower flow in small streams  

- **Seasonal deficits (3–6 months / SPI-3 to SPI-6, SPEI-3 to SPEI-6)**  
  → Lower river discharge, reduced reservoir storage, early signs of water scarcity  

- **Long-term deficits (6–12+ months / SPI-6 to SPI-12, SPEI-6 to SPEI-12)**  
  → Reduced groundwater recharge, declining aquifer levels, long-lasting hydrological drought  

In practice:

- **SPI** remains one of the most robust indicators of **meteorological drought**, as it responds directly to precipitation anomalies.  
- **SPEI** links **meteorological and agricultural drought**, capturing temperature-driven evaporative demand and heat-related intensification.  
- **Long-term SPI and SPEI (e.g., 12-month)** are often used as early indicators of a **developing hydrological drought**, reflecting sustained deficits across seasons.

Together, these indices provide complementary insights into how drought emerges, evolves, and impacts different components of the water cycle.

---

---

## Why drought indices?

Raw precipitation values alone don’t tell us whether a region is experiencing drought — is 50 mm of rainfall in a month “normal,” “too little,” or “a lot”?  
To answer such questions, drought indices compare current conditions to typical long-term patterns and express **how unusual** they are.

Drought indices help us:
- Compare regions with very different climates  
- Detect emerging drought early  
- Monitor severity and persistence  
- Support decision-making in agriculture, water management, and risk assessment  

---

## The Standardized Precipitation Index (SPI)

The **Standardized Precipitation Index (SPI)** (McKee et al., 1993) is one of the simplest and most widely used drought indicators.

**What it measures:**  
SPI quantifies precipitation anomalies over a chosen accumulation period relative to a long-term climatology.

Common accumulation periods:
- **SPI-1** → short-term meteorological dryness  
- **SPI-3** → seasonal impacts  
- **SPI-12** → long-term hydrological stress  

**Interpretation (WMO, 2012):**

| SPI value      | Interpretation        |
|----------------|------------------------|
| > 2.0          | Extremely wet          |
| 1.5–1.99       | Very wet               |
| 1.0–1.49       | Moderately wet         |
| -0.99–0.99     | Near normal            |
| -1.0–-1.49     | Moderately dry         |
| -1.5–-1.99     | Severely dry           |
| < -2.0         | Extremely dry          |

**Strengths**
- Simple, robust  
- Requires only precipitation  
- Comparable across climates  

**Limitations**
- Does **not** consider temperature or evaporative demand  

---

## The Standardized Precipitation–Evapotranspiration Index (SPEI)

The **SPEI** (Vicente-Serrano et al., 2010) extends SPI by including temperature-driven **evaporative demand**, which is especially relevant under climate warming.

**What it measures:**  
It uses a simple climatic water balance:

> **Water balance = Precipitation – Potential Evapotranspiration (PET)**

Hotter conditions increase PET, lowering the water balance even when rainfall is unchanged — SPEI captures this effect.

**Advantages**
- Accounts for temperature effects  
- Sensitive to heat-driven drought intensification  
- Flexible timescales (1–48 months)

**Limitations**
- Requires PET estimation (method-dependent)  
- Slightly more complex than SPI  

---

## Further reading and authoritative sources

### Scientific and methodological references
- WMO (2012). *Standardized Precipitation Index User Guide.*  
- McKee, T. B., Doesken, N. J., & Kleist, J. (1993). *The relationship of drought frequency and duration to time scales.*  
- Vicente-Serrano, S. M., Beguería, S., & López-Moreno, J. I. (2010). *A multiscalar drought index sensitive to global warming.*  

### Operational drought monitoring
- **Global Drought Observatory (GDO)**: https://edo.jrc.ec.europa.eu/gdo  
- **European Drought Observatory (EDO)**: https://edo.jrc.ec.europa.eu/  

These platforms provide real-time maps, long-term records, and multiple drought indicators.

---

```{admonition} Summary
SPI and SPEI are core indices for understanding meteorological drought.  
Knowing the difference between meteorological, agricultural, and hydrological drought provides essential context in the climate rist framework.
```
---

## References

- FAO (2013). *Agricultural Drought.*  
- Gibbs, W. J., & Maher, J. V. (1967). *Rainfall deciles as drought indicators.*  
- McKee, T. B., Doesken, N. J., & Kleist, J. (1993). *The relationship of drought frequency and duration to time scales.*  
- Van Loon, A. F. (2015). *Hydrological drought explained.*  
- Vicente-Serrano, S. M., Beguería, S., & López-Moreno, J. I. (2010). *SPEI: A new global drought index.*  
- WMO (2012). *Standardized Precipitation Index User Guide.*  

