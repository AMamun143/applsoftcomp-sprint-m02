"""Load 1d-data.csv. Used for format step; viz script reads CSV directly."""
import pandas as pd
DATA_PATH = "data/1d-data.csv"

def load():
    return pd.read_csv(DATA_PATH)

if __name__ == "__main__":
    df = load()
    print(df.shape, df.columns.tolist())
