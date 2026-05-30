from pathlib import Path
import pandas as pd


def load_csv(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Arquivo CSV não encontrado: {path}")
    return pd.read_csv(path)
