"""
Visualize 1d-multi-method-data.csv: AUC-ROC by method; highlight Proposed.
Output: figs/fig-1d-multi-method.png
"""
import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = "data/1d-multi-method-data.csv"
FIG_PATH = "figs/fig-1d-multi-method.png"

def main():
    df = pd.read_csv(DATA_PATH)
    means = df.groupby("method", sort=False)["AUCROC"].mean()
    # Order: Proposed first, then Baseline_1, ..., Baseline_9
    order = ["Proposed"] + [f"Baseline_{i}" for i in range(1, 10)]
    means = means.reindex([m for m in order if m in means.index])
    colors = ["#1f77b4" if m == "Proposed" else "lightgray" for m in means.index]
    fig, ax = plt.subplots(figsize=(8, 5))
    means.plot(kind="barh", ax=ax, color=colors, edgecolor="black", linewidth=0.5)
    ax.set_xlabel("AUC-ROC")
    ax.set_ylabel("Method")
    ax.set_title("AUC-ROC by method (Proposed highlighted)")
    ax.set_xlim(0, 1)
    fig.tight_layout()
    fig.savefig(FIG_PATH, dpi=150)
    plt.close()
    print(f"Saved {FIG_PATH}")

if __name__ == "__main__":
    main()
