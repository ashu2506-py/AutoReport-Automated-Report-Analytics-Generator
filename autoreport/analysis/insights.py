import pandas as pd


def generate_insights(df: pd.DataFrame):

    insights = {}

    # Total Revenue
    if "Quantity" in df.columns and "Price" in df.columns:
        df["Revenue"] = df["Quantity"] * df["Price"]
        insights["total_revenue"] = df["Revenue"].sum()

    # Top Selling Product
    if "Product" in df.columns and "Quantity" in df.columns:
        top = df.loc[df["Quantity"].idxmax()]
        insights["top_product"] = top["Product"]
        insights["top_quantity"] = top["Quantity"]

    # Revenue by Product
    if "Product" in df.columns and "Revenue" in df.columns:
        insights["revenue_by_product"] = (
            df.groupby("Product")["Revenue"]
            .sum()
            .sort_values(ascending=False)
        )

    # Average Price
    if "Price" in df.columns:
        insights["average_price"] = df["Price"].mean()

    return insights