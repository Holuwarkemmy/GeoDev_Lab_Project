# Data Preparation

## Working CRS

The project uses EPSG:32631, WGS 84 / UTM Zone 31N as the working coordinate reference system.

This CRS was selected because Eti-Osa is within UTM Zone 31N and the projected system uses metres. It is therefore suitable for distance, area, road-length, slope and other metric calculations. The source datasets were mainly in EPSG:4326 and were reprojected to EPSG:32631 for analysis.

## Data Reprojected

The following datasets were reprojected to EPSG:32631:

- Eti-Osa LGA boundary
- Eti-Osa ward boundaries
- GRID3 settlement extents
- OSM waterways
- OSM water bodies
- OSM road network
- GRID3 health facilities
- SRTM DEM
- WorldPop population count raster

The vector datasets were consolidated into an analysis-ready GeoPackage. The DEM and population raster were processed separately.

## Data Clipped

The Eti-Osa LGA boundary was used as the study-area mask.

The following were clipped to the study area:

- Ward boundaries
- Settlement extents
- Waterways
- Water bodies
- Road network
- Health facilities
- DEM
- Population count raster

The LGA boundary itself was retained as the main study-area boundary.

## Five Quality Checks

### Check 1: CRS consistency
Reprojected vector data, DEM and population raster use **EPSG:32631**.

### Check 2: Study-area extent

The processed datasets were clipped using the Eti-Osa LGA boundary and restricted to the required study area.

### Check 3: Geometry validity

Vector layers were checked for geometry issues that could affect clipping and spatial overlay. The analysis-ready layers are prepared for subsequent spatial processing.

### Check 4: Missing/null attributes

- Several OSM attributes are sparse or null.
- The main fields required for analysis, including `highway` for roads and `waterway` for waterways, were retained.

### Check 5: Raster quality and NoData

**DEM:**
- CRS: EPSG:32631
- Approximate resolution: 30 m
- Elevation unit: metres
- Recorded source elevation range: -13 m to 35 m
- Final NoData value: `n/a`

**Population count:**
- CRS: EPSG:32631
- Resolution: 100 m
- Original NoData value: `-3.40282e+38`
- Reprojected and clipped to the study area.
- Reprojected NoData value: `-99999`

### DEM slope calculation

Slope calculated directly from the DEM in EPSG:4326 produced unrealistic statistics.

**Action:** Reprojected the DEM to EPSG:32631 and recalculated slope.

**Corrected slope statistics:**
- Minimum: 0
- Maximum: 22.82207