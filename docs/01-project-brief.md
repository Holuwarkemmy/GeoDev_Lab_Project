# Project brief

**Week 1 deliverable.** GeoDev Lab Africa, Cohort One.
Author: Akanbi Saheedat

## 1. The question

> How can flood risk zones in Eti-Osa LGA be mapped and quantified in terms of exposed population and critical infrastructure?

## 2. Why this question

Eti-Osa LGA has the largest proportion of land at high flood risk in Lagos at 79.38%, with studies confirming it as one of the most vulnerable areas in the state due to its low-lying coastal topography. Urban planners and emergency management agencies would use these maps to prioritize flood defense infrastructure investment, restrict development in very high vulnerability zones, and plan evacuation routes.

## 3. Study area

Eti-Osa Local Government Area, Lagos State, Nigeria. The boundary comes from the GRID3 Operational LGA Boundaries dataset, with ward-level breakdowns from the matching GRID3 ward boundaries.

## 4. What I mean by the terms

- **Flood hazard** is a weighted overlay of elevation, slope, and distance to water. Land that is low, flat, and close to a river or drainage channel scores higher.
- **Exposed population** is the estimated number of people, from WorldPop's 100m population count, whose location falls inside a given hazard class.
- **Critical infrastructure** covers health facilities and road segments that fall inside high or very-high hazard zones, the places where flooding would cut off care or movement, not just damage property.

## 5. Datasets

| # | Dataset | What it gives me | Source |
|---|---|---|---|
| 1 | GRID3 Operational LGA Boundaries | Eti-Osa administrative boundary | <https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries/about> |
| 2 | GRID3 Operational Wards Boundaries | Ward-level units for analysis and reporting | <https://data.grid3.org/datasets/GRID3::grid3-nga-operational-wards-v1-0/about> |
| 3 | WorldPop population count (100m) | Population density for exposure estimates | <https://www.worldpop.org> |
| 4 | GRID3 Settlement Extents v4.1 | Built-up areas and building footprints | <https://data.grid3.org/datasets/GRID3::grid3-nga-settlement-extents-v4-1/about> |
| 5 | SRTM DEM (30m) | Elevation and slope for the hazard model | <https://www.portal.opentopography.org> |
| 6 | OpenStreetMap hydrology | Rivers, streams, and drainage for water-proximity analysis | <https://www.openstreetmap.org> |
| 7 | OpenStreetMap road network | Roads for exposure and evacuation-route analysis | <https://www.openstreetmap.org> |
| 8 | GRID3 Health Facilities v2.0 | Health facility locations for critical infrastructure exposure | <https://data.grid3.org/datasets/GRID3::grid3-nga-health-facilities-v2-0/about> |

## 6. What "done" looks like

An interactive dashboard with three layers people can actually click through: a flood hazard map from the weighted overlay, a population exposure layer showing roughly how many people sit in each risk class, and a critical infrastructure layer marking health facilities and roads inside high-risk zones. Anyone should be able to select a ward and pull a short exposure report out of it.

## 7. Known risks

**OSM completeness.** The road and waterway layers come from OpenStreetMap, and outside the main highways and named rivers, most of the attribute fields are sparse. If a minor drainage channel was never mapped, it simply won't show up in the hazard model.


**Status:** Week 1 complete. Data acquisition in Week 2, see [02-data-notes.md](02-data-notes.md).
