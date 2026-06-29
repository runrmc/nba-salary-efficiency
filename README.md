# Bang for the Buck: Modeling NBA Player Performance to Contract Value

## Overview
Do NBA teams win because they spend more, or because they spend more efficiently? This project
examines a decade of player-season data to identify which players are over- or undervalued
relative to their on-court performance, whether contract-year incentives produce measurable
changes in play, and whether younger players are systematically underpaid under the NBA's
rookie salary scale.

## Research Questions
- Can a player's "fair" salary be estimated from their stats, and who looks most over- or undervalued?
- Are younger players more systematically underpaid by the market?
- Do players produce more in contract years and less after signing?

## Key Findings
- OLS regression predicting salary cap percentage from performance metrics achieved R² ≈ 0.60,
  with FGM/G, minutes, PIE, and USG% as the strongest predictors — volume stats outpaced
  efficiency metrics as salary drivers
- Residual analysis identified players like Ben Simmons and Gordon Hayward as significantly
  overpaid, and Pascal Siakam and Desmond Bane as significantly underpaid; in the latter cases,
  the residual reflects a structural feature of the CBA rather than a market mispricing
- Contract year analysis found no significant performance bump in most metrics — only TS%
  showed a significant increase (p = 0.004, +1.19%), suggesting players prioritize shot quality
  and efficiency over volume in the year before a new contract
- Players aged 19–22 show a salary index of 0.41 against a performance index of 0.91,
  producing near league-average impact while earning less than half the league-average pay share,
  driven by the NBA's rookie salary scale

## Data Sources
- **NBA API** — player advanced stats via the `LeagueDashPlayerStats` endpoint
  (2016–17 through 2025–26 seasons); 5,492 raw records across 10 seasons
- **Basketball Reference** — player salary data scraped across all 30 teams and 10 seasons
  (300 requests); normalized to salary cap percentage for cross-season comparability
- Inner join on a shared key produced 3,268 matched records; applying filters of ≥ 1% salary
  cap and ≥ 500 minutes yielded a final analytical sample of 2,973 player-seasons

## Methods
- Custom data pipeline joining NBA API and Basketball Reference on a
  `{first4}_{last}_{team}_{year}` key
- OLS regression via `statsmodels`
- Independent samples t-tests for contract year analysis
- Visualizations built in `matplotlib`

## Project Structure

```
nba-salary-efficiency/
├── src/
│   ├── 01_stats_pipeline.ipynb
│   ├── 02_salary_pipeline.ipynb
│   ├── 03_join_clean_data.ipynb
│   ├── 04_eda_visuals.ipynb
│   ├── 05_simple_regression.ipynb
│   ├── nba_project_utils.py
│   ├── requirements.txt
│   └── data/
│       ├── *.csv
│       └── figures/
|           ├── *.png
└── nba_modeling_project_report.pdf
```

## Setup

```bash
pip install -r src/requirements.txt
```

Player stats are pulled via the `nba_api` Python package. Run `01_stats_pipeline.ipynb`
first to fetch and cache the data locally.

Note: the salary scraper (`02_salary_pipeline.ipynb`) must be run locally due to
Cloudflare restrictions on Basketball Reference.

## Authors
Ryan McCurry, Yuki Kodama, and Quentinn Roby — MADS Program, University of Michigan, 2026
