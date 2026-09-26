# Data notes

**Week 2 deliverable.** GeoDev Lab Africa, Cohort One.
Author: Akanbi Saheedat

What I downloaded, where it came from, what is in it, and what is wrong with it.

All raw vector layers are stored together in `data/raw/Eti_Osa.gpkg`. The DEM and population raster are kept as separate GeoTIFFs.

## Summary

| # | Dataset | Type | Retrieved | Status |
|---|---|---|---|---|
| 1 | Eti-Osa Administrative Boundary | Vector (polygon) | 9 Sep 2026 | OK |
| 2 | Eti-Osa Ward Boundaries | Vector (polygon) | 9 Sep 2026 | OK |
| 3 | Settlement Extents | Vector (polygon) | 9 Sep 2026 | OK |
| 4 | Waterways | Vector (line) | 9 Sep 2026 | OK |
| 5 | Water Bodies | Vector (polygon) | 9 Sep 2026 | OK |
| 6 | Road Network | Vector (line) | 9 Sep 2026 | OK |
| 7 | Health Facilities | Vector (point) | 9 Sep 2026 | OK |
| 8 | Population Count Raster | Raster | 12 Sep 2026 | OK |
| 9 | Digital Elevation Model | Raster | 12 Sep 2026 | OK |

---

## 1. Eti-Osa Administrative Boundary

- **Source:** GRID3 Operational LGA Boundaries
- **Retrieved:** 9 September 2026
- **File:** `data/raw/Eti_Osa.gpkg`
- **Format:** GeoPackage
- **Geometry type:** Polygon
- **Feature count:** 1
- **CRS as downloaded:** EPSG:4326

**Key columns**

| Column | What it holds | Nulls |
|---|---|---|
| `lganame` / `lgacode` | LGA name and code | none noted |
| `statename` / `statecode` | State name and code | none noted |
| `shape_Are` / `shape_Len` | Source-provided area and perimeter | none noted |

**What I noticed**

Just the one polygon, which is exactly what is needed. It is the mask everything else gets clipped to.

## 2. Eti-Osa Ward Boundaries

- **Source:** GRID3 NGA Operational Wards Boundaries
- **Retrieved:** 9 September 2026
- **File:** `data/raw/Eti_Osa.gpkg`
- **Format:** GeoPackage
- **Geometry type:** Polygon
- **Feature count:** 20
- **CRS as downloaded:** EPSG:4326

**Key columns**

| Column | What it holds | Nulls |
|---|---|---|
| `wardname` / `wardcode` | Ward name and code | none |
| `lganame` / `lgacode` | Parent LGA name and code | none |
| `urban` | Source-provided urban classification | none |

**What I noticed**

`wardname` is complete across all 20 wards, which matters because it is the field exposure statistics will be joined to later.

## 3. Settlement Extents

- **Source:** GRID3 NGA Settlement Extent v4.1
- **Retrieved:** 9 September 2026
- **File:** `data/raw/Eti_Osa.gpkg`
- **Format:** GeoPackage
- **Geometry type:** Polygon
- **Feature count:** 5,903
- **CRS as downloaded:** EPSG:4326

**Key columns**

| Column | What it holds |
|---|---|---|
| `block_id`, `block_area_sqm`, `block_perimeter` | Settlement block identity and size |
| `building_count`, `building_area_min/max/sum/median/stdev` | Building-level stats per block |
| `extent_type`, `bd_class`, `ma_class`, `composite_class` | Settlement/building classifications | 

**What I noticed**

This is a much richer dataset than expected, nearly 6,000 blocks with building-level area statistics attached. That level of detail will allow to distinguish dense residential settlement from lighter development during the exposure analysis, rather than treating every built-up block the same.


## 4. Waterways

- **Source:** OpenStreetMap via QuickOSM
- **Query:** `waterway=*`
- **Retrieved:** 9 September 2026
- **File:** `data/raw/Eti_Osa.gpkg`
- **Format:** GeoPackage
- **Geometry type:** Line
- **Feature count:** 534
- **CRS as downloaded:** EPSG:4326

**Key columns**

| Column | What it holds | Nulls |
|---|---|---|
| `waterway` | Waterway classification | none |
| `name` | Waterway name where available | many |
| `boat`, `tunnel`, `layer` | OSM attributes, present where mapped | many |

**What I noticed**

`name` is null for a lot of the smaller channels, which is normal for OSM, minor drainage lines rarely get named. The `waterway` field itself is well populated.

## 5. Water Bodies

- **Source:** OpenStreetMap via QuickOSM
- **Queries:** `natural=water`, `natural=wetland`
- **Retrieved:** 9 September 2026
- **File:** `data/raw/Eti_Osa.gpkg`
- **Format:** GeoPackage
- **Geometry type:** Polygon
- **Feature count:** 55
- **CRS as downloaded:** EPSG:4326

**Key columns**

| Column | What it holds | Nulls |
|---|---|---|
| `natural` | Water/wetland classification | none|
| `water` | Water feature sub-type where available | some |
| `name` | Water body name where available | some |

**What I noticed**

The layer is smaller than expected at 55 features, but it fills the gaps the waterway lines leave, lagoon edges and wetland patches especially, which matter for a coastal LGA like this one.

## 6. Road Network

- **Source:** OpenStreetMap via QuickOSM
- **Query:** `highway=*`
- **Retrieved:** 9 September 2026
- **File:** `data/raw/Eti_Osa.gpkg`
- **Format:** GeoPackage
- **Geometry type:** Line
- **Feature count:** 11,940
- **CRS as downloaded:** EPSG:4326

**Key columns**

| Column | What it holds | Nulls |
|---|---|---|
| `highway` | Road classification | none |
| `name` | Road name where available | many |
| `bridge` | Bridge attribute where available | many |

**What I noticed**

Nearly 12,000 line segments, but most fields beyond `highway` and `osm_id` are sparse.

## 7. Health Facilities

- **Source:** GRID3 NGA Health Facilities v2.0
- **Retrieved:** 9 September 2026
- **File:** `data/raw/Eti_Osa.gpkg`
- **Format:** GeoPackage
- **Geometry type:** Point
- **Feature count:** 138
- **CRS as downloaded:** EPSG:4326

**Key columns**

| Column | What it holds | Nulls |
|---|---|---|
| `facility_name`, `facility_level`, `facility_level_option` | Facility identity and level | none |
| `ownership`, `ownership_type` | Ownership information | none |
| `ward`, `lga`, `state` | Administrative location | none |

**What I noticed**

138 facilities across the LGA, geocoded and ward-tagged.

## 8. Population Count Raster

- **Source:** `nga_pop_2025_CN_100m_R2025A_v1`, WorldPop
- **Retrieved:** 12 September 2026
- **File:** `data/raw/nga_pop_2025_100m.tif`
- **Format:** GeoTIFF
- **Resolution:** 100m
- **CRS as downloaded:** EPSG:4326
- **NoData value:** -99999
- **Value range:** 0.01694 to 150.067 people per pixel

**What I noticed**

The fractional values (0.017 up to 150) are a reminder this is a modeled surface, not a literal head count per pixel, WorldPop distributes census totals down to the grid using ancillary layers. Fine for relative exposure comparisons between wards.

## 9. Digital Elevation Model

- **Source:** SRTM 1 Arc-Second Global (~30m), via OpenTopography
- **Retrieved:** 12 September 2026
- **File:** `data/raw/srtm_eti_osa.tif`
- **Format:** GeoTIFF
- **Resolution:** ~30m
- **CRS as downloaded:** EPSG:4326
- **Elevation range:** -13m to 35m

**What I noticed**

A 48-metre spread across the entire LGA is about as flat as it gets, which fits Eti-Osa's coastal, low-lying reputation, but it also means slope derived from this DEM will be a blunt instrument.

## Cross-cutting problems

**Everything arrived in a different native resolution.** Vector layers, a 100m population raster, and a 30m DEM don't combine directly, nothing gets overlaid until all of it is reprojected and, for the rasters, resampled onto a consistent grid.

**OSM attribute sparsity.** Beyond the core classification fields (`highway`, `waterway`, `natural`), most OSM attributes across the roads, waterways, and water bodies layers are inconsistently populated. Analysis will designed around the fields that are reliably present.


**Status:** Week 2 complete. Reprojection and quality checks in Week 3, see [03-data-preparation.md](03-data-preparation.md).
