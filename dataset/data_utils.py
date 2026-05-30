from pathlib import Path
import pandas as pd


def load_dataset(csv_path):
    csv_path = Path(csv_path)
    if not csv_path.exists():
        raise FileNotFoundError(f"Dataset not found: {csv_path}")
    return pd.read_csv(csv_path)


def summarize_dataset(df):
    return {
        "shape": df.shape,
        "columns": df.columns.tolist(),
        "missing_values": df.isna().sum().to_dict(),
        "description": df.describe(include="all").to_dict(),
    }
