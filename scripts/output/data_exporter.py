from pathlib import Path
import pandas as pd


def export_summary_csv(df, out_path):
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.describe(include="all").to_csv(out_path)
    return out_path


def save_histogram(df, column, output_path):
    try:
        import matplotlib.pyplot as plt
    except ImportError as error:
        raise ImportError("matplotlib é necessário para salvar histogramas. Instale com pip install matplotlib") from error

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(8, 5))
    df[column].dropna().plot(kind="hist", title=f"Histograma de {column}")
    plt.xlabel(column)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    return output_path
