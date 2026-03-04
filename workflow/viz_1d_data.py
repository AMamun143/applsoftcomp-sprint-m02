"""
Visualize 1d-data.csv: treatment effect (cases vs control).
Output: figs/fig-1d-data.png
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Paths relative to project root (run from repo root)
DATA_PATH = "data/1d-data.csv"
FIG_PATH = "figs/fig-1d-data.png"

def main():
    df = pd.read_csv(DATA_PATH)
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(data=df, x="group", y="value", ax=ax)
    ax.set_xlabel("Group")
    ax.set_ylabel("Value")
    ax.set_title("Treatment effect: cases vs control")
    fig.tight_layout()
    fig.savefig(FIG_PATH, dpi=150)
    plt.close()
    print(f"Saved {FIG_PATH}")

if __name__ == "__main__":
    main()
