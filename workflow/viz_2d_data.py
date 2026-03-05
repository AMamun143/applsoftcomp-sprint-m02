"""
Visualize 2d-data.csv: 2D density (hexbin).
Output: figs/fig-2d-data.png
"""
import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = "data/2d-data.csv"
FIG_PATH = "figs/fig-2d-data.png"

def main():
    df = pd.read_csv(DATA_PATH)
    fig, ax = plt.subplots(figsize=(6, 5))
    hb = ax.hexbin(df["x"], df["y"], gridsize=25, cmap="Blues", mincnt=1)
    fig.colorbar(hb, ax=ax, label="Count")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("2D data density")
    ax.set_aspect("equal")
    fig.tight_layout()
    fig.savefig(FIG_PATH, dpi=150)
    plt.close()
    print(f"Saved {FIG_PATH}")

if __name__ == "__main__":
    main()
