import pandas as pd


def trend_analysis(df: pd.DataFrame):

    trends = {}

    numeric_columns = df.select_dtypes(include="number").columns

    for column in numeric_columns:

        trends[column] = {
            "moving_average": df[column].rolling(window=3).mean(),
            "growth_rate": df[column].pct_change() * 100
        }

    return trends