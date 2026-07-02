import os
import matplotlib.pyplot as plt
import seaborn as sns


def generate_charts(df, charts):

    os.makedirs("../reports/charts", exist_ok=True)

    # ---------------- BAR CHART ----------------
    if "bar" in charts and {"Product", "Quantity"}.issubset(df.columns):

        plt.figure(figsize=(8, 5))
        plt.bar(df["Product"], df["Quantity"])

        plt.title("Product vs Quantity")
        plt.xlabel("Product")
        plt.ylabel("Quantity")

        plt.tight_layout()
        plt.savefig("../reports/charts/bar_chart.png")
        plt.close()

    else:
        if "bar" in charts:
            print("Skipping Bar Chart (Product, Quantity not found)")

    # ---------------- LINE CHART ----------------
    if "line" in charts and {"Product", "Price"}.issubset(df.columns):

        plt.figure(figsize=(8, 5))
        plt.plot(df["Product"], df["Price"], marker="o")

        plt.title("Product vs Price")
        plt.xlabel("Product")
        plt.ylabel("Price")

        plt.tight_layout()
        plt.savefig("../reports/charts/line_chart.png")
        plt.close()

    else:
        if "line" in charts:
            print("Skipping Line Chart (Product, Price not found)")

    # ---------------- PIE CHART ----------------
    if "pie" in charts and {"Product", "Quantity"}.issubset(df.columns):

        plt.figure(figsize=(6, 6))
        plt.pie(
            df["Quantity"],
            labels=df["Product"],
            autopct="%1.1f%%"
        )

        plt.title("Quantity Distribution")

        plt.tight_layout()
        plt.savefig("../reports/charts/pie_chart.png")
        plt.close()

    else:
        if "pie" in charts:
            print("Skipping Pie Chart (Product, Quantity not found)")

    # ---------------- SCATTER ----------------
    if "scatter" in charts and {"Quantity", "Price"}.issubset(df.columns):

        plt.figure(figsize=(8, 5))
        plt.scatter(df["Quantity"], df["Price"])

        plt.title("Quantity vs Price")
        plt.xlabel("Quantity")
        plt.ylabel("Price")

        plt.tight_layout()
        plt.savefig("../reports/charts/scatter_chart.png")
        plt.close()

    else:
        if "scatter" in charts:
            print("Skipping Scatter Chart (Quantity, Price not found)")

    # ---------------- HEATMAP ----------------
    if "heatmap" in charts:

        numeric_df = df.select_dtypes(include="number")

        if len(numeric_df.columns) >= 2:

            plt.figure(figsize=(8, 6))

            sns.heatmap(
                numeric_df.corr(),
                annot=True,
                cmap="Blues",
                linewidths=0.5
            )

            plt.title("Correlation Heatmap")

            plt.tight_layout()
            plt.savefig("../reports/charts/heatmap_chart.png")
            plt.close()

        else:
            print("Skipping Heatmap (Not enough numeric columns)")

    # ---------------- REVENUE ----------------
    if (
        "revenue" in charts
        and {"Product", "Quantity", "Price"}.issubset(df.columns)
    ):

        temp = df.copy()

        temp["Revenue"] = temp["Quantity"] * temp["Price"]

        revenue = (
            temp.groupby("Product")["Revenue"]
            .sum()
            .sort_values(ascending=False)
        )

        plt.figure(figsize=(8, 5))

        revenue.plot(kind="bar")

        plt.title("Revenue by Product")
        plt.xlabel("Product")
        plt.ylabel("Revenue")

        plt.tight_layout()
        plt.savefig("../reports/charts/revenue_chart.png")
        plt.close()

    else:
        if "revenue" in charts:
            print("Skipping Revenue Chart")

    # ---------------- TREND ----------------
    if (
        "trend" in charts
        and {"Quantity", "Price"}.issubset(df.columns)
    ):

        temp = df.copy()

        temp["Revenue"] = temp["Quantity"] * temp["Price"]

        plt.figure(figsize=(8, 5))

        plt.plot(temp["Revenue"], marker="o")

        plt.title("Revenue Trend")
        plt.xlabel("Record")
        plt.ylabel("Revenue")

        plt.grid(True)

        plt.tight_layout()
        plt.savefig("../reports/charts/trend_chart.png")
        plt.close()

    else:
        if "trend" in charts:
            print("Skipping Trend Chart")

    print("Charts Generated Successfully!")