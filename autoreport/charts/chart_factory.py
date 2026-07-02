import os
import matplotlib.pyplot as plt
import seaborn as sns


def generate_charts(df,charts):
    os.makedirs("../reports/charts", exist_ok=True)

    # Bar Chart
    if "bar" in charts:
        plt.figure(figsize=(8, 5))
        plt.bar(df["Product"], df["Quantity"])
        plt.title("Product vs Quantity")
        plt.xlabel("Product")
        plt.ylabel("Quantity")
        plt.tight_layout()
        plt.savefig("../reports/charts/bar_chart.png")
        plt.close()

    # Line Chart
    if "line" in charts:
        plt.figure(figsize=(8, 5))
        plt.plot(df["Product"], df["Price"], marker="o")
        plt.title("Product vs Price")
        plt.xlabel("Product")
        plt.ylabel("Price")
        plt.tight_layout()
        plt.savefig("../reports/charts/line_chart.png")
        plt.close()

    # Pie Chart
    if "pie" in charts:
        plt.figure(figsize=(6, 6))
        plt.pie(df["Quantity"], labels=df["Product"], autopct="%1.1f%%")
        plt.title("Quantity Distribution")
        plt.savefig("../reports/charts/pie_chart.png")
        plt.close()

    # Scatter Plot
    if "scatter" in charts:
        plt.figure(figsize=(8, 5))
        plt.scatter(df["Quantity"], df["Price"])
        plt.title("Quantity vs Price")
        plt.xlabel("Quantity")
        plt.ylabel("Price")
        plt.tight_layout()
        plt.savefig("../reports/charts/scatter_chart.png")
        plt.close()
    
    # Heatmap
    if "heatmap" in charts:

        numeric_df = df.select_dtypes(include="number")

        if not numeric_df.empty:

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

    print("Charts Generated Successfully!")