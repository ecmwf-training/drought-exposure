# FAIR Principles

```{admonition} What does FAIR mean?
:class: note
The FAIR principles — **Findable, Accessible, Interoperable, and Reusable** — provide a framework for making scientific data and software as useful as possible, both for humans and machines. See {cite}`wilkinson2016fair` for an overview of the FAIR principes for scientific data. 
```

## This jupyter book is FAIR because:

**It's Findable.** The source code is publicly available on [GitHub](https://github.com/jkeune/extreme_precip_exposure) under a stable URL, and the book is rendered as a public website. All input datasets are drawn from catalogued, citeable repositories (Copernicus CDS, GHS, Eurostat/NUTS).

**It's Accessible.** The book requires no local software installation: notebooks can be executed directly in the browser, for example via [Binder](https://mybinder.org). Input data are either bundled with the repository or freely downloadable from open data portals. The book itself is published under an open-access policy.

**It's Interoperable.** All data are stored in open, community-standard formats — NetCDF for gridded climate fields and CSV for derived tabular outputs. Region geometries use the official NUTS shapefile provided by Eurostat. The analysis relies exclusively on well-documented, open-source Python libraries.

**It's Reusable.** The code is released under the [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) licence, allowing others to freely use, modify, and redistribute it. How-to guides document each processing step in a reproducible way, and the explanation section provides the conceptual background needed to adapt the workflow to other hazards or regions.