import os
import matplotlib.pyplot as plt
import seaborn as sns


OUTPUT_DIR = "../reports/charts"


def save_chart(filename):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, filename))
    plt.close()


def generate_charts(df, charts):

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    columns = set(df.columns)

    is_sales = {"Product", "Quantity", "Price"}.issubset(columns)

    is_hr = {
        "Department",
        "Salary",
        "PerformanceScore"
    }.issubset(columns)

    is_inventory = {
        "Product",
        "Category",
        "Stock",
        "UnitPrice"
    }.issubset(columns)

    # =====================================================
    # SALES DATASET
    # =====================================================

    if is_sales:

        print("Sales Dataset Detected")

        # ---------------- BAR ----------------

        if "bar" in charts:

            plt.figure(figsize=(8,5))

            plt.bar(df["Product"], df["Quantity"])

            plt.title("Product vs Quantity")

            plt.xlabel("Product")

            plt.ylabel("Quantity")

            save_chart("bar_chart.png")

        # ---------------- LINE ----------------

        if "line" in charts:

            plt.figure(figsize=(8,5))

            plt.plot(
                df["Product"],
                df["Price"],
                marker="o",
                linewidth=3
            )

            plt.title("Product vs Price")

            plt.xlabel("Product")

            plt.ylabel("Price")

            plt.grid(True)

            save_chart("line_chart.png")

        # ---------------- PIE ----------------

        if "pie" in charts:

            plt.figure(figsize=(7,7))

            plt.pie(
                df["Quantity"],
                labels=df["Product"],
                autopct="%1.1f%%",
                startangle=90
            )

            plt.title("Quantity Distribution")

            save_chart("pie_chart.png")

        # ---------------- SCATTER ----------------

        if "scatter" in charts:

            plt.figure(figsize=(8,5))

            plt.scatter(
                df["Quantity"],
                df["Price"],
                s=120
            )

            plt.xlabel("Quantity")

            plt.ylabel("Price")

            plt.title("Quantity vs Price")

            plt.grid(True)

            save_chart("scatter_chart.png")

        # ---------------- REVENUE ----------------

        if "revenue" in charts:

            temp = df.copy()

            temp["Revenue"] = (
                temp["Quantity"] *
                temp["Price"]
            )

            revenue = (
                temp.groupby("Product")["Revenue"]
                .sum()
                .sort_values(ascending=False)
            )

            plt.figure(figsize=(8,5))

            revenue.plot(kind="bar")

            plt.title("Revenue by Product")

            plt.ylabel("Revenue")

            save_chart("revenue_chart.png")

        # ---------------- TREND ----------------

        if "trend" in charts:

            plt.figure(figsize=(8,5))

            plt.plot(
                temp["Revenue"],
                marker="o",
                linewidth=3
            )

            plt.title("Revenue Trend")

            plt.xlabel("Record")

            plt.ylabel("Revenue")

            plt.grid(True)

            save_chart("trend_chart.png")
            
                # =====================================================
    # HR DATASET
    # =====================================================

    elif is_hr:

        print("HR Dataset Detected")

        # ---------------- BAR ----------------

        if "bar" in charts:

            salary = df.groupby("Department")["Salary"].mean()

            plt.figure(figsize=(8,5))

            salary.plot(kind="bar")

            plt.title("Average Salary by Department")

            plt.xlabel("Department")

            plt.ylabel("Average Salary")

            save_chart("bar_chart.png")

        # ---------------- LINE ----------------

        if "line" in charts:

            plt.figure(figsize=(8,5))

            plt.plot(
                df["Salary"],
                marker="o",
                linewidth=3
            )

            plt.title("Salary Distribution")

            plt.xlabel("Employee")

            plt.ylabel("Salary")

            plt.grid(True)

            save_chart("line_chart.png")

        # ---------------- PIE ----------------

        if "pie" in charts:

            dept = df["Department"].value_counts()

            plt.figure(figsize=(7,7))

            plt.pie(
                dept,
                labels=dept.index,
                autopct="%1.1f%%",
                startangle=90
            )

            plt.title("Employees by Department")

            save_chart("pie_chart.png")

        # ---------------- SCATTER ----------------

        if "scatter" in charts:

            plt.figure(figsize=(8,5))

            plt.scatter(
                df["Salary"],
                df["PerformanceScore"],
                s=120
            )

            plt.xlabel("Salary")

            plt.ylabel("Performance Score")

            plt.title("Salary vs Performance")

            plt.grid(True)

            save_chart("scatter_chart.png")


    # =====================================================
    # INVENTORY DATASET
    # =====================================================

    elif is_inventory:

        print("Inventory Dataset Detected")

        # ---------------- BAR ----------------

        if "bar" in charts:

            plt.figure(figsize=(9,5))

            plt.bar(
                df["Product"],
                df["Stock"]
            )

            plt.xticks(rotation=45)

            plt.title("Available Stock")

            plt.xlabel("Product")

            plt.ylabel("Stock")

            save_chart("bar_chart.png")

        # ---------------- LINE ----------------

        if "line" in charts:

            plt.figure(figsize=(8,5))

            plt.plot(
                df["Stock"],
                marker="o",
                linewidth=3
            )

            plt.title("Stock Trend")

            plt.xlabel("Product")

            plt.ylabel("Stock")

            plt.grid(True)

            save_chart("line_chart.png")

        # ---------------- PIE ----------------

        if "pie" in charts:

            category = df["Category"].value_counts()

            plt.figure(figsize=(7,7))

            plt.pie(
                category,
                labels=category.index,
                autopct="%1.1f%%",
                startangle=90
            )

            plt.title("Products by Category")

            save_chart("pie_chart.png")

        # ---------------- SCATTER ----------------

        if "scatter" in charts:

            plt.figure(figsize=(8,5))

            plt.scatter(
                df["Stock"],
                df["UnitPrice"],
                s=120
            )

            plt.xlabel("Stock")

            plt.ylabel("Unit Price")

            plt.title("Stock vs Unit Price")

            plt.grid(True)

            save_chart("scatter_chart.png")
            
                # =====================================================
    # GENERIC DATASET
    # =====================================================

    else:

        print("Generic Dataset Detected")

        numeric_cols = df.select_dtypes(include="number").columns.tolist()
        categorical_cols = df.select_dtypes(include="object").columns.tolist()

        # ---------------- BAR ----------------

        if (
            "bar" in charts
            and len(categorical_cols) >= 1
            and len(numeric_cols) >= 1
        ):

            plt.figure(figsize=(9,5))

            plt.bar(
                df[categorical_cols[0]],
                df[numeric_cols[0]]
            )

            plt.xticks(rotation=45)

            plt.title(
                f"{categorical_cols[0]} vs {numeric_cols[0]}"
            )

            plt.tight_layout()

            save_chart("bar_chart.png")

        # ---------------- LINE ----------------

        if "line" in charts and len(numeric_cols) >= 1:

            plt.figure(figsize=(8,5))

            plt.plot(
                df[numeric_cols[0]],
                marker="o",
                linewidth=3
            )

            plt.title(f"{numeric_cols[0]} Trend")

            plt.grid(True)

            save_chart("line_chart.png")

        # ---------------- PIE ----------------

        if "pie" in charts and len(categorical_cols) >= 1:

            values = df[categorical_cols[0]].value_counts()

            plt.figure(figsize=(7,7))

            plt.pie(
                values,
                labels=values.index,
                autopct="%1.1f%%",
                startangle=90
            )

            plt.title(
                f"{categorical_cols[0]} Distribution"
            )

            save_chart("pie_chart.png")

        # ---------------- SCATTER ----------------

        if "scatter" in charts and len(numeric_cols) >= 2:

            plt.figure(figsize=(8,5))

            plt.scatter(
                df[numeric_cols[0]],
                df[numeric_cols[1]],
                s=120
            )

            plt.xlabel(numeric_cols[0])

            plt.ylabel(numeric_cols[1])

            plt.grid(True)

            plt.title(
                f"{numeric_cols[0]} vs {numeric_cols[1]}"
            )

            save_chart("scatter_chart.png")

    # =====================================================
    # HEATMAP (COMMON)
    # =====================================================

    if "heatmap" in charts:

        numeric_df = df.select_dtypes(include="number")

        if len(numeric_df.columns) >= 2:

            plt.figure(figsize=(10,7))

            sns.heatmap(
                numeric_df.corr(),
                annot=True,
                cmap="Blues",
                linewidths=.5,
                fmt=".2f"
            )

            plt.title("Correlation Heatmap")

            save_chart("heatmap_chart.png")

        else:

            print("Skipping Heatmap (Need at least 2 numeric columns)")

    print("\nCharts Generated Successfully!")