"""Load 2d-data.csv."""
import pandas as pd
DATA_PATH = "data/2d-data.csv"

def load():
    return pd.read_csv(DATA_PATH)

if __name__ == "__main__":
    df = load()
    print(df.shape, df.columns.tolist())
