# Data preparation

**Week 3 deliverable.** GeoDev Lab Africa, Cohort One.
Author: Akanbi Saheedat

What I reprojected, what I clipped, what I checked, and what I fixed.

## 1. Coordinate system decisions

**Working CRS:** EPSG:32631, WGS 84 / UTM Zone 31N

**Why this one:** Eti-Osa sits inside UTM Zone 31N, and this projection is in metres, so distance, area, road-length, and slope calculations all come out in real units instead of degrees. Every source dataset arrived in EPSG:4326 and was reprojected from there.

| Dataset | CRS as downloaded | CRS after | Operation |
|---|---|---|---|
| Eti-Osa LGA boundary | EPSG:4326 | EPSG:32631 | Reprojected |
| Eti-Osa ward boundaries | EPSG:4326 | EPSG:32631 | Reprojected |
| Settlement extents | EPSG:4326 | EPSG:32631 | Reprojected |
| Waterways | EPSG:4326 | EPSG:32631 | Reprojected |
| Water bodies | EPSG:4326 | EPSG:32631 | Reprojected |
| Road network | EPSG:4326 | EPSG:32631 | Reprojected |
| Health facilities | EPSG:4326 | EPSG:32631 | Reprojected |
| SRTM DEM | EPSG:4326 | EPSG:32631 | Reprojected |
| WorldPop population raster | EPSG:4326 | EPSG:32631 | Reprojected |

> Reprojecting recalculates every coordinate. Assigning a CRS only relabels the data. Everything above was actually reprojected, not just relabelled.

## 2. Clipping to the study area

- **Boundary used:** Eti-Osa LGA boundary, GRID3 Operational LGA Boundaries
- **Clipped:** ward boundaries, settlement extents, waterways, water bodies, road network, health facilities, DEM, population raster
- **Kept as-is:** the LGA boundary itself, used as the reference extent for every other layer

## 3. The five quality checks

| Check | Result | Action taken |
|---|---|---|
| Is the CRS what I think it is? | Yes | Confirmed EPSG:32631 across all reprojected vectors and rasters |
| Are there nulls in the fields I need? | Some, in optional OSM fields | Core fields (`highway`, `waterway`) retained clean; sparse fields left as-is, not used in analysis |
| Are there duplicate features? | No duplicate features | Confirmed that none of the layers contain duplicate features |
| Is the geometry valid? | No issues found | Vector layers checked and confirmed valid for clipping and overlay |
| Does coverage span the whole study area? | Yes | All layers clipped to and consistent with the Eti-Osa boundary |

## 4. Problems found, and what I did

**DEM slope came out wrong the first time.** The slope was initially calculated directly from the DEM while it was still in EPSG:4326, and the statistics that came back were unrealistic for terrain this flat. The fix was to reproject the DEM to EPSG:32631 first and recalculate from there. Corrected slope ranges from 0 to 22.82, which is far more plausible for Eti-Osa's low-relief coastline.

Lesson noted: reproject before deriving anything from a DEM, not after.

## 5. The analysis-ready output

- **File:**
`data/processed/Eti_Osa_utm31N.gpkg` (vector layers)
`data/processed/Eti_Osa_DEM_utm_31N`
`data/processed/Eti_Osa_Pop_count_2025_utm31N`
`data/processed/Eti_Osa_Slope_utm31N`
- **Format:** GeoPackage (vectors), GeoTIFF (rasters)
- **CRS:** EPSG:32631 throughout
- **Produced by:** manually in QGIS


**Status:** Week 3 complete. First spatial analysis in Week 4, see [04-water-proximity-analysis.md](04-water-proximity-analysis.md).
