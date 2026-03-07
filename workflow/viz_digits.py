"""
Visualize digits-data.csv: t-SNE 2D embedding colored by digit.
Output: figs/fig-digits.png
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

DATA_PATH = "data/digits-data.csv"
FIG_PATH = "figs/fig-digits.png"

def main():
    df = pd.read_csv(DATA_PATH)
    feature_cols = [c for c in df.columns if c.startswith("pixel_")]
    X = df[feature_cols].values
    y = df["digit"].values
    tsne = TSNE(n_components=2, random_state=42)
    X_2d = tsne.fit_transform(X)
    fig, ax = plt.subplots(figsize=(8, 6))
    scatter = ax.scatter(X_2d[:, 0], X_2d[:, 1], c=y, cmap="tab10", s=8, alpha=0.7)
    ax.set_xlabel("t-SNE 1")
    ax.set_ylabel("t-SNE 2")
    ax.set_title("UCI digits: 2D t-SNE colored by digit")
    plt.colorbar(scatter, ax=ax, label="Digit")
    fig.tight_layout()
    fig.savefig(FIG_PATH, dpi=150)
    plt.close()
    print(f"Saved {FIG_PATH}")

if __name__ == "__main__":
    main()
