# Eti-Osa Flood Exposure Mapping

Maps flood hazard zones across Eti-Osa LGA, Lagos, and quantifies how many people, health facilities, and roads sit inside them, so planners can see where flood defenses and evacuation routes matter most.

**GeoDev Lab Africa, Cohort One.** Akanbi Saheedat


## The question

> How can flood risk zones in Eti-Osa LGA be mapped and quantified in terms of exposed population and critical infrastructure?

## What this answers so far

> Within the selected 50m waterway and 100m water-body proximity zones, 1,532 of 5,903 settlement extents, 2,563 of 11,940 road features, and 10 of 138 health facilities in Eti-Osa fall inside the water-proximity zone.

This is a proximity result, not the final flood-risk result, the hazard model still needs elevation, slope, and a documented weighting method before that stronger claim can be made.

## The four weeks

| Week | What it covers | Doc |
|---|---|---|
| 1 | The question, study area, and every dataset with a source link | [01-project-brief.md](docs/01-project-brief.md) |
| 2 | What was downloaded, its structure, and what's wrong with it | [02-data-notes.md](docs/02-data-notes.md) |
| 3 | Reprojection, clipping, and five quality checks | [03-data-preparation.md](docs/03-data-preparation.md) |
| 4 | The water-proximity buffer analysis and its result | [04-water-proximity-analysis.md](docs/04-water-proximity-analysis.md) |

Map: [water_buffer_exposure.png](maps/water_buffer_exposure.png)

## What's in here

```
GeoDev_Lab_Project/
├── docs/
│   ├── 01-project-brief.md              Week 1
│   ├── 02-data-notes.md                 Week 2
│   ├── 03-data-preparation.md           Week 3
│   └── 04-water-proximity-analysis.md   Week 4
├── data/
│   ├── raw/                             downloads
│   └── processed/                       outputs
├── analysis/                            Week 4 outputs (gpkg)
├── maps/                                exported map images
├── scripts/                             codes/notebooks
└── requirements.txt                     required libaries
```

## How to run it

```bash
git clone https://github.com/holuwarkemmy/GeoDev_Lab_Project.git
cd GeoDev_Lab_Project

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

The data is not in this repository. Every source is linked in [the project brief](docs/01-project-brief.md), so anyone can fetch it.

## Progress

- [x] Week 1, project brief with a source link for every dataset
- [x] Week 2, data downloaded, opened and described
- [x] Week 3, reprojected, clipped and quality checked
- [x] Week 4, first spatial analysis, checked four ways


Akanbi Saheedat · GeoDev Lab Africa
Learn. Build. Collaborate. Transform.
