# Flood Exposure Mapping for Eti-Osa Local Government Area, Lagos

## 1. Question

How can flood risk zones in Eti-Osa LGA be mapped and quantified in terms of exposed population and critical infrastructure?

## 2. Why It Matters

Eti-Osa LGA has the largest proportion of land at high flood risk in Lagos at 79.38%, with studies confirming it as one of the most vulnerable areas in the state due to its low-lying coastal topography. Urban planners and emergency management agencies would use these maps to prioritize flood defense infrastructure investment, restrict development in very high vulnerability zones, and plan evacuation routes.

## 3. Data Required

- Eti-Osa administrative boundary
- Eti-Osa ward administrative boundary
- Population density data at 100m resolution
- Settlement extents showing built-up areas and infrastructure footprints
- Digital Elevation Model (DEM) for slope and elevation analysis
- Hydrology data (rivers, water bodies, drainage networks)
- Road network for evacuation route planning
- Health facility locations for critical infrastructure risk assessment

## 4. Data Source

- Eti-Osa administrative boundary - [GRID3 NGA - Operational LGA Boundaries](https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries/about)
- Eti-Osa ward administrative boundary - [GRID3 NGA - Operational Wards Boundaries](https://data.grid3.org/datasets/GRID3::grid3-nga-operational-wards-v1-0/about)
- Population density (100m) - [WorldPop](https://www.worldpop.org)
- Settlement extents v4.1 - [GRID3](https://data.grid3.org/datasets/GRID3::grid3-nga-settlement-extents-v4-1/about)
- SRTM DEM (30m) - [USGS EarthExplorer](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.usgs.gov/centers/eros/science/usgs-eros-archive-digital-elevation-shuttle-radar-topography-mission-srtm&ved=2ahUKEwj53ou2o9eWAxXvdUEAHfXKH4QQFnoECCEQAQ&sqi=2&usg=AOvVaw1Mun6O700tYNVUVFv4TE5Q)
- Hydrology (Rivers/Waterway) - [OpenStreetMap](https://www.openstreetmap.org)
- Road network - [OpenStreetMap](https://www.openstreetmap.org)
- Health facilities - [GRID3](https://data.grid3.org/datasets/GRID3::grid3-nga-health-facilities-v2-0/about)

## 5. Deliverable

An interactive web dashboard with three integrated layers: a flood hazard map derived from weighted overlay analysis of elevation, slope, and proximity to water; a population exposure overlay showing an estimate number of people in each risk zone; and a critical infrastructure layer identifying health facilities and roads within high-risk areas. The product will allow users to click on any ward to view exposure statistics and download per-ward risk reports for planning agencies.
