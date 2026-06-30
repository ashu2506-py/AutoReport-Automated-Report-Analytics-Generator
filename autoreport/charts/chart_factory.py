import os
import matplotlib.pyplot as plt


def generate_charts(df):
    os.makedirs("reports/charts", exist_ok=True)

    # Bar Chart
    plt.figure(figsize=(8, 5))
    plt.bar(df["Product"], df["Quantity"])
    plt.title("Product vs Quantity")
    plt.xlabel("Product")
    plt.ylabel("Quantity")
    plt.tight_layout()
    plt.savefig("reports/charts/bar_chart.png")
    plt.close()

    # Line Chart
    plt.figure(figsize=(8, 5))
    plt.plot(df["Product"], df["Price"], marker="o")
    plt.title("Product vs Price")
    plt.xlabel("Product")
    plt.ylabel("Price")
    plt.tight_layout()
    plt.savefig("reports/charts/line_chart.png")
    plt.close()

    # Pie Chart
    plt.figure(figsize=(6, 6))
    plt.pie(df["Quantity"], labels=df["Product"], autopct="%1.1f%%")
    plt.title("Quantity Distribution")
    plt.savefig("reports/charts/pie_chart.png")
    plt.close()

    # Scatter Plot
    plt.figure(figsize=(8, 5))
    plt.scatter(df["Quantity"], df["Price"])
    plt.title("Quantity vs Price")
    plt.xlabel("Quantity")
    plt.ylabel("Price")
    plt.tight_layout()
    plt.savefig("reports/charts/scatter_chart.png")
    plt.close()

    print("Charts Generated Successfully!")