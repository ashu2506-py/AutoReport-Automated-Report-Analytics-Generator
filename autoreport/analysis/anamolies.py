import pandas as pd
import numpy as np


def detect_anomalies(df: pd.DataFrame):

    anomalies = {}

    numeric_columns = df.select_dtypes(include="number").columns

    for column in numeric_columns:
        mean = df[column].mean()
        std = df[column].std()

        if std != 0:
            z_scores = (df[column] - mean) / std
            anomalies[column] = {
                "z_score": df[np.abs(z_scores) > 3]
            }

        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)

        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        anomalies[column]["iqr"] = df[
            (df[column] < lower) |
            (df[column] > upper)
        ]

    return anomalies