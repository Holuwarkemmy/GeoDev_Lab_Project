# Water-proximity analysis

**Week 4 deliverable.** GeoDev Lab Africa, Cohort One.
Author: Akanbi Saheedat

The first real spatial operation: a water-proximity buffer, and what it catches.

## 1. The operation

A buffer-and-merge workflow, run in the working CRS, EPSG:32631, WGS 84 / UTM Zone 31N.

- A **50m buffer** around the waterways layer
- A **100m buffer** around the water bodies layer
- The two buffers **merged into one water-proximity polygon**

## 2. Why this operation

Proximity to water is one of the planned flood-susceptibility factors, and running it first give a simple, defensible screen for which settlements, roads, and health facilities sit close to mapped water, before elevation and slope get folded in.

## 3. Expectation before running it

Going in, the merged buffer is expected to cover a modest slice of the LGA and therefore pull back a subset of each layer, not everything. The source data going into the extraction was:

| Dataset | Source features |
|---|---:|
| Waterways | 534 |
| Water bodies | 55 |
| Settlement extents | 5,903 |
| Roads | 11,940 |
| Health facilities | 138 |

## 4. Result

| Dataset | Source features | Features in buffer |
|---|---:|---:|
| Settlement extents | 5,903 | **1,532** |
| Roads | 11,940 | **2,563** |
| Health facilities | 138 | **10** |

## 5. What this tells us

1,532 settlement extents, 2,563 road segments, and 10 health facilities fall inside the merged 50m/100m water-proximity zone. 

Worth being precise about what it means, though: this is a proximity result, not a flood-risk result. Sitting within 50m of a waterway or 100m of a water body does not by itself mean a feature will flood, it just means it is close enough that water proximity should count against it once the full hazard model is built.

## 6. Quality checks, four ways

**Map check.** Exported the merged buffer alongside the extracted settlements, roads, and health facilities to confirm visually that the extraction lines up with what the buffer geometry should catch.

**Row-count check.** Extracted layers hold 1,532 settlement extents, 2,563 roads, and 10 health facilities, matching the numbers in the result table above.

**Manual feature check.** Cross-checked the health facilities against the buffer by hand, since 10 is a small enough set to verify one by one. The extracted layer holds exactly those 10.

**Empty-geometry check.** Reviewed the extracted road and health-facility layers for empty or null geometries. None found.

## 8. Files

- `analysis/04_water_buffer_analysis.gpkg`
- `maps/water_buffer_exposure.png`


**Status:** Week 4 complete, and Month 1 done with.