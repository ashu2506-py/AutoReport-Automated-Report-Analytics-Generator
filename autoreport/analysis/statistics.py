import pandas as pd

def generate_statistics(df: pd.DataFrame):
    return {
        "shape": df.shape,
        "columns": df.columns.tolist(),
        "summary": df.describe(include="all"),
        "missing_values": df.isnull().sum(),
        "duplicates": df.duplicated().sum()
    }