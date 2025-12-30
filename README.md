# NBA 3-Point Efficiency vs Volume Analysis (2024–2025)

## Overview
This project analyzes whether NBA team success during the 2024–2025 season is more strongly correlated with three-point shooting **efficiency** or **volume**. Team success is measured using **Net Rating**, a possession-adjusted performance metric.

## Data
The CSV's used in this project are from basketball-reference.com

- **Player-level statistics** (shooting, games played, team assignments)
- **Team-level statistics** (wins, losses, net rating, rankings)

Mid-season trades are explicitly handled to avoid double-counting player contributions.

## Methodology
1. Cleaned player data by removing aggregate trade rows (e.g., `2TM`, `3TM`)
2. Converted player shooting stats into per-team season contributions
3. Aggregated three-point makes and attempts at the team level
4. Computed team three-point percentage
5. Evaluated correlations between:
   - 3P% and Net Rating
   - 3PA and Net Rating
6. Visualized relationships using scatter plots with linear regression lines

## Results
- **3P% vs Net Rating:** r ≈ 0.67 (moderately strong correlation)
- **3PA vs Net Rating:** r ≈ 0.14 (weak correlation)

This indicates that **shooting efficiency** is a much stronger predictor of team success than shot volume alone.

## Notable Observations
- Boston serves as a high-volume outlier that performs well without elite efficiency
- This suggests extreme volume can partially compensate for lower efficiency, though the effect is not consistent league-wide

## Tools Used
- Python
- Pandas
- NumPy
- Matplotlib

## Conclusion
During the 2024 - 2025 NBA season, a team's 3-point shooting percentage matters far more than how many 3's they are attempting (in terms of net rating).
