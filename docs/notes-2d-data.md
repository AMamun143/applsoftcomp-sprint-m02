# Notes: 2D Data

## Data structure

- **File:** `data/2d-data.csv`
- **Columns:** `x`, `y`; ~6000 points (2D measurements).

## Key observations

- Dense point cloud; scatter would be overplotted. Density-based view (hexbin or 2D histogram) is more informative.

## Visualization strategy

- **Choice:** Hexbin plot to show density without overplotting. Axis labels "x" and "y".
- I used **Claude** to compare options (scatter, heatmap, contour, hexbin) and to generate the initial `plt.hexbin()` call; I set axis labels and figure path.
- I used **ChatGPT** to check best practices for hexbin grid size so the plot is not too coarse or noisy.

## AI usage

- **Claude:** Dense 2D visualization options and hexbin boilerplate.
- **ChatGPT:** Hexbin bin count / gridsize best practices.
