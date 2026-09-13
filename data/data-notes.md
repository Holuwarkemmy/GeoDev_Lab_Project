# Flood Exposure Mapping for Eti-Osa Local Government Area, Lagos

This document describes the spatial datasets used for the Eti-Osa flood exposure mapping project, including their sources, geometry, coordinate reference systems, important attributes, and intended analytical use.
All the vector layers are inside 'Eti Osa GeoPackage' file in data folder.

## 1. Eti-Osa Administrative LGA Boundary

- Source: [GRID3 - Operational LGA Boundaries](https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries) 
- Date downloaded - September 9, 2026
- Geometry: Polygon 
- CRS: EPSG:4326 - WGS 84
- Important fields: lganame - string, lgacode - string, statename - string, statecode - string, shape_Are - real, shape_Len - real
- Purpose: Defines the overall study area and provides the boundary used to constrain and clip other datasets.

## 2. Eti-Osa Ward Boundaries

- Source: [GRID3 NGA - Operational Wards Boundaries](https://data.grid3.org/datasets/GRID3::grid3-nga-operational-wards-v1-0)
- Date downloaded - September 9, 2026
- Geometry: Polygon 
- CRS: EPSG:4326 - WGS 84
- Total Features: 20
- Important fields: fid - int, wardname - string, wardcode - string, lganame - string, lgacode - string, statename - string, statecode - string, urban - string
- No null in wardname

## 3. Settlement Extents

- Source: [GRID3 NGA Settlement Extent v4.1](https://data.grid3.org/datasets/GRID3::grid3-nga-settlement-extents-v4-1) 
- Date downloaded - September 9, 2026
- Geometry: Polygon  
- CRS: EPSG:4326 - WGS 84
- Total features: 5,903
- Important fields: block_id - string, block_area_sqm - real, block_perimeter - real, building_count- integer, building_area_min - real, building_area_max - real, building_area_sum - real, building_area_median - real, building_area_stdev - real, building_area_percentage - real, extent_type - string, bd_class - string, ma_class - string, composite_class - string, Shape__Area - real, Shape__Length - real

## 4. Waterways

- Source: OpenStreetMap via QuickOSM  
- Geometry: Line  
- Query: 'waterway=*'
- CRS: EPSG:4326 - WGS 84
- Total features: 534
- Date acquired - September 9, 2026
- Important fields: fid - integer, full_id - string, osm_id - string, osm_type - string, waterway - string, boat - string, tunnel - string, layer - string, name - string

## 5. Water Bodies
  
- Source: OpenStreetMap via QuickOSM  
- Geometry: Polygon  
- Query: 'natural=water', 'natural=wetland'
- Total features: 55
- Date acquired - September 9, 2026
- CRS: EPSG:4326 - WGS 84
- Important fields: fid - integer, full_id - string, osm_id - string, osm_type - string, natural - string, water - string, name - string
- Name field contain some null values

## 6. Road Network

- Source: OpenStreetMap via QuickOSM  
- Geometry: Line  
- Query: 'highway=*'
- CRS: EPSG:4326 - WGS 84
- Total features: 11940
- Date acquired - September 9, 2026
- Important fields: full_id - string, osm_id - string, osm_type - string, highway - string, bridge - string, name - string
- Apart from the main fields, most of the remaining fields have many null values or are sparsely populated
- Purpose: Represents the road and transport network within the study area.

## 7. Health Facilities
 
- Source: [GRID3 - NGA Health Facilities v2.0](https://data.grid3.org/datasets/GRID3::grid3-nga-health-facilities-v2-0) 
- Geometry: Point
- CRS: EPSG:4326 - WGS 84
- Total features: 137
- Date downloaded - September 9, 2026
- Important fields: OBJECTID - integer, state - string, lga - string, ward - string, facility_name - string, ownership - string, ownership_type - string, facility_level - string, facility_level_option - string, latitude - real, longitude - real
- Purpose: Identifies health facilities that may be exposed to flood hazards and can therefore be considered critical infrastructure.

## 8. Population Count Raster 

- Source: [WorldPop (nga_pop_2023_CN_100m_R2025A_v1)](https://www.worldpop.org)
- Date downloaded - September 12, 2026
- Geometry: Raster  
- Resolution: 100 m 
- CRS: EPSG:4326 - WGS 84  
- Dataset year: 2025
- Pixel size: 0.0008333333323943662753,-0.0008333333262411321031
- Minimum value - 0.01694
- Maximum value - 150.067
- NoData value: -99999

## 9. Digital Elevation Model (DEM)
  
- Source: [USGS / NASA Shuttle Radar Topography Mission (SRTM)](https://www.portal.opentopography.org)
- Date downloaded - September 12, 2026
- Geometry: Raster  
- Resolution: Approximately 30 m  
- Elevation unit: Metres
- CRS: EPSG:4326 - WGS 84
- Pixel size: 0.0002694945852994556088,-0.0002694945850340138061
- Minimum elevation: -13 m
- Maximum elevation: 35 m
- NoData value - n/a