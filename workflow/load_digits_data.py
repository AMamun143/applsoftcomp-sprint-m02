"""Load digits-data.csv (or sklearn load_digits)."""
import pandas as pd
DATA_PATH = "data/digits-data.csv"

def load():
    return pd.read_csv(DATA_PATH)

if __name__ == "__main__":
    df = load()
    feats = [c for c in df.columns if c.startswith("pixel_")]
    print(df.shape, len(feats), "features", "digit" in df.columns)
