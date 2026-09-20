# Data Notes

This document describes the spatial datasets used for the Flood Hazard and Exposure Mapping for Eti-Osa Local Government Area, Lagos project. It records the source, acquisition date, geometry, CRS, important attributes, intended use, and relevant data limitations.

All raw vector layers are stored in the **Eti_Osa.gpkg** in the `data/raw` folder.

## Data Inventory

| Dataset | Source | Geometry | CRS | Features / Resolution | Main Use |
|---|---|---|---|---:|---|
| Eti-Osa Administrative Boundary | GRID3 Operational LGA Boundaries | Polygon | EPSG:4326 | 1 | Study area boundary |
| Eti-Osa Ward Boundaries | GRID3 NGA Operational Wards Boundaries | Polygon | EPSG:4326 | 20 | Ward-level analysis |
| Settlement Extents | GRID3 NGA Settlement Extent v4.1 | Polygon | EPSG:4326 | 5,903 | Built-up/settlement exposure |
| Waterways | OpenStreetMap via QuickOSM | Line | EPSG:4326 | 534 | Distance-to-water analysis |
| Water Bodies | OpenStreetMap via QuickOSM | Polygon | EPSG:4326 | 55 | Water/wetland proximity |
| Road Network | OpenStreetMap via QuickOSM | Line | EPSG:4326 | 11,940 | Road exposure and transport analysis |
| Health Facilities | GRID3 NGA Health Facilities v2.0 | Point | EPSG:4326 | 137 | Critical infrastructure exposure |
| Population Count Raster | WorldPop | Raster | EPSG:4326 | 100 m | Population exposure |
| Digital Elevation Model | SRTM | Raster | EPSG:4326 | ~30 m | Elevation and slope analysis |

# 1. Eti-Osa Administrative LGA Boundary

### Source
- **Dataset:** GRID3 Operational LGA Boundaries
- **Downloaded:** 9 September 2026

### Spatial Information
- **Geometry:** Polygon
- **CRS:** EPSG:4326, WGS 84
- **Feature count:** 1

### Important Fields

| Field | Type | Description |
|---|---|---|
| `lganame` | String | Local Government Area name |
| `lgacode` | String | Local Government Area code |
| `statename` | String | State name |
| `statecode` | String | State code |
| `shape_Are` | Real | Source-provided area field |
| `shape_Len` | Real | Source-provided perimeter/length field |

### Intended Use
Defines the Eti-Osa study area and provides the boundary used to constrain, clip, and analyse other datasets.

# 2. Eti-Osa Ward Boundaries

### Source
- **Dataset:** GRID3 NGA Operational Wards Boundaries
- **Downloaded:** 9 September 2026

### Spatial Information
- **Geometry:** Polygon
- **CRS:** EPSG:4326, WGS 84
- **Feature count:** 20

### Important Fields

| Field | Type | Description |
|---|---|---|
| `fid` | Integer | GeoPackage/QGIS feature identifier |
| `wardname` | String | Ward name |
| `wardcode` | String | Ward code |
| `lganame` | String | Local Government Area name |
| `lgacode` | String | Local Government Area code |
| `statename` | String | State name |
| `statecode` | String | State code |
| `urban` | String | Urban classification field provided by the source |

`wardname` contains no null values in the dataset.

### Intended Use
Provides the administrative units for ward-level flood hazard and exposure statistics, mapping, and reporting.

# 3. Settlement Extents

### Source
- **Dataset:** GRID3 NGA Settlement Extent v4.1
- **Downloaded:** 9 September 2026

### Spatial Information
- **Geometry:** Polygon
- **CRS:** EPSG:4326, WGS 84
- **Feature count:** 5,903

### Important Fields

| Field | Type | Description |
|---|---|---|
| `block_id` | String | Settlement/block identifier |
| `block_area_sqm` | Real | Area of the settlement/block in square metres |
| `block_perimeter` | Real | Perimeter of the settlement/block |
| `building_count` | Integer | Number of mapped buildings associated with the block |
| `building_area_min` | Real | Minimum mapped building area |
| `building_area_max` | Real | Maximum mapped building area |
| `building_area_sum` | Real | Total mapped building area |
| `building_area_median` | Real | Median mapped building area |
| `building_area_stdev` | Real | Standard deviation of mapped building area |
| `building_area_percentage` | Real | Percentage of the block area occupied by mapped buildings |
| `extent_type` | String | Settlement extent classification |
| `bd_class` | String | Building-related classification |
| `ma_class` | String | Source classification field |
| `composite_class` | String | Composite settlement/building classification |
| `Shape__Area` | Real | Source-provided geometry area field |
| `Shape__Length` | Real | Source-provided geometry length field |

### Intended Use
Represents mapped settlement extents and built-up areas. It is used to identify settlements intersecting flood hazard zones and quantify settlement exposure.

# 4. Waterways

### Source
- **Dataset:** OpenStreetMap via QuickOSM
- **Query:** `waterway=*`
- **Downloaded:** 9 September 2026

### Spatial Information
- **Geometry:** Line
- **CRS:** EPSG:4326, WGS 84
- **Feature count:** 534

### Important Fields

| Field | Type | Description |
|---|---|---|
| `fid` | Integer | GeoPackage/QGIS feature identifier |
| `full_id` | String | OpenStreetMap feature identifier |
| `osm_id` | String | OpenStreetMap object identifier |
| `osm_type` | String | OpenStreetMap object type |
| `waterway` | String | Waterway classification |
| `boat` | String | Boat-related OSM attribute where available |
| `tunnel` | String | Tunnel-related OSM attribute where available |
| `layer` | String | OSM layer information where available |
| `name` | String | Waterway name where available |

- Some fields contain null values.

### Intended Use
Represents mapped rivers, streams, drainage channels, and other linear waterways. It is primarily used to calculate distance to water/drainage as part of the flood hazard model.

# 5. Water Bodies

### Source
- **Dataset:** OpenStreetMap via QuickOSM
- **Queries:** `natural=water` and `natural=wetland`
- **Downloaded:** 9 September 2026

### Spatial Information
- **Geometry:** Polygon
- **CRS:** EPSG:4326, WGS 84
- **Feature count:** 55

### Important Fields

| Field | Type | Description |
|---|---|---|
| `fid` | Integer | GeoPackage/QGIS feature identifier |
| `full_id` | String | OpenStreetMap feature identifier |
| `osm_id` | String | OpenStreetMap object identifier |
| `osm_type` | String | OpenStreetMap object type |
| `natural` | String | Natural feature classification |
| `water` | String | Water feature classification where available |
| `name` | String | Water body name where available |

The `name` field is null for some of the water bodies.

### Intended Use
Represents mapped surface-water and wetland areas. It complements the waterway layer and can be used in water-proximity analysis and interpretation of flood-prone areas.

# 6. Road Network

### Source
- **Dataset:** OpenStreetMap via QuickOSM
- **Query:** `highway=*`
- **Downloaded:** 9 September 2026

### Spatial Information
- **Geometry:** Line
- **CRS:** EPSG:4326, WGS 84
- **Feature count:** 11,940

### Important Fields

| Field | Type | Description |
|---|---|---|
| `full_id` | String | OpenStreetMap feature identifier |
| `osm_id` | String | OpenStreetMap object identifier |
| `osm_type` | String | OpenStreetMap object type |
| `highway` | String | Road/highway classification |
| `bridge` | String | Bridge attribute where available |
| `name` | String | Road name where available |

Most other available fields are sparse or contain many null values.

### Intended Use
Represents the mapped road and transport network. It is used to identify roads intersecting or located within flood hazard zones and to support interpretation of transport exposure.

# 7. Health Facilities

### Source
- **Dataset:** GRID3 NGA Health Facilities v2.0
- **Downloaded:** 9 September 2026

### Spatial Information
- **Geometry:** Point
- **CRS:** EPSG:4326, WGS 84
- **Feature count:** 138

### Important Fields

| Field | Type | Description |
|---|---|---|
| `OBJECTID` | Integer | Source feature identifier |
| `state` | String | State name |
| `lga` | String | Local Government Area name |
| `ward` | String | Ward name |
| `facility_name` | String | Health facility name |
| `ownership` | String | Facility ownership information |
| `ownership_type` | String | Ownership classification |
| `facility_level` | String | Facility level |
| `facility_level_option` | String | Facility level classification/option |
| `latitude` | Real | Facility latitude |
| `longitude` | Real | Facility longitude |

### Intended Use
Identifies health facilities that may be exposed to flood hazards. The layer supports assessment of the number and location of health facilities within different flood hazard classes.

### Data Limitation
Facility attributes and operational information reflect the source dataset and may not represent current conditions at the time of analysis.

# 8. Population Count Raster

### Source
- **Dataset:** `nga_pop_2023_CN_100m_R2025A_v1`
- **Provider:** WorldPop
- **Downloaded:** 12 September 2026

### Spatial Information
- **Data type:** Raster
- **Resolution:** 100 m
- **CRS:** EPSG:4326, WGS 84
- **Pixel size:** `0.0008333333323943662753, -0.0008333333262411321031`
- **NoData value:** `-99999`

### Raster Statistics Recorded

- **Minimum value:** `0.01694`
- **Maximum value:** `150.067`

### Intended Use
Used to estimate the population exposed to different flood hazard zones and to derive population exposure statistics by ward.

# 9. Digital Elevation Model

### Source
- **Dataset:** SRTM 1 Arc-Second Global, approximately 30 m
- **Original data source:** NASA Shuttle Radar Topography Mission (SRTM)
- **Access/download source:** OpenTopography
- **Downloaded:** 12 September 2026

### Spatial Information
- **Data type:** Raster
- **Approximate resolution:** 30 m
- **Elevation unit:** metres
- **CRS:** EPSG:4326, WGS 84
- **Pixel size:** `0.0002694945852994556088, -0.0002694945850340138061`
- **NoData value:** `n/a`

### Raster Statistics

- **Minimum elevation:** -13 m
- **Maximum elevation:** 35 m

### Intended Use
Provides elevation data for deriving terrain variables, particularly elevation and slope, for the flood hazard model.
