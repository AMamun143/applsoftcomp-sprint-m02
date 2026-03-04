# Notes: 1D Data (Treatment Effect)

## Data structure

- **File:** `data/1d-data.csv`
- **Columns:** `value`, `group`
- **Groups:** `cases` (10 rows), `control` (10 rows)
- **Interpretation:** Effect of a treatment for 10 subjects per group.

## Key observations

- Values span a wide range. Two-group comparison is the main question.
- Visualization should emphasize cases vs control (e.g., side-by-side box plot).

## Visualization strategy

- **Choice:** Side-by-side box plot with `group` on the x-axis and `value` on the y-axis.
- I used **ChatGPT** to help choose between a violin plot and a box plot for this small two-group dataset. ChatGPT suggested a box plot for n=10 per group; I implemented the box plot.
- I used **Claude** to generate the initial matplotlib/seaborn boilerplate for reading the CSV and creating the box plot, then I adjusted labels, title, and output path.

## AI usage

- **ChatGPT:** Choice between violin plot and box plot; decided on box plot for small n.
- **Claude:** Initial matplotlib/seaborn code for CSV load and box plot; I modified labels and paths.
