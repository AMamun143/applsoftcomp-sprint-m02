# Notes: 1D Multi-Method Data (AUC-ROC)

## Data structure

- **File:** `data/1d-multi-method-data.csv`
- **Columns:** `method`, `AUCROC`
- **Methods:** Proposed, Baseline_1 … Baseline_9; 10 AUC-ROC values per method.
- **Goal:** Highlight "Proposed" against baselines using preattentive encoding.

## Visualization strategy

- **Choice:** Bar chart of mean AUC-ROC per method. Proposed in a standout color; baselines in light gray. Proposed placed first (position + color).
- I used **ChatGPT** to decide how to highlight one method (color vs border vs size) and to get an example of coloring one bar differently in matplotlib.
- I used **Claude** to generate the pandas groupby/aggregation and bar plot structure; I added the color logic and labels.

## AI usage

- **ChatGPT:** How to highlight one bar; matplotlib color example.
- **Claude:** groupby mean AUC-ROC and bar plot boilerplate; I added color and labels.
