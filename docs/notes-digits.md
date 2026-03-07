# Notes: UCI ML Hand-Written Digits

## Data structure

- **File:** `data/digits-data.csv` (or `sklearn.datasets.load_digits()`)
- **Content:** 8×8 pixel images, 64 features + `digit` (0–9). 1797 samples.
- **Goal:** Visualize in 2D; color by digit class (use given labels, no clustering).

## Visualization strategy

- **Choice:** Scatter plot of t-SNE 2D embedding, colored by digit. Colormap tab10 for 10 classes.
- I used **Claude** to get code for loading digits, running t-SNE, and scatter plot colored by digit; I adjusted figure size, legend, and output path.
- I used **ChatGPT** to choose colormap (tab10 vs viridis) for 10 discrete classes; used tab10.

## AI usage

- **Claude:** Load digits, t-SNE, scatter colored by digit.
- **ChatGPT:** Colormap for 10 discrete classes (tab10).
