import os
import typer
import pandas as pd
from pathlib import Path
from analysis.statistics import generate_statistics
from charts.chart_factory import generate_charts
from report.html_report import generate_html
from report.pdf_report import generate_pdf
from report.template_loader import load_template
from injestion.data_loader import load_data
from scheduler.scheduler import start_scheduler
from analysis.insights import generate_insights
from analysis.trends import trend_analysis
from analysis.anamolies import detect_anomalies

app=typer.Typer()
@app.command()
def hello():
    print("Welcome to Auto Report")
    
@app.command()
def generate(file: str, template: str,table:str=None):
    os.makedirs("reports/charts", exist_ok=True)
    config = load_template(template)

    df = load_data(file,table)
    

    if config["include_statistics"]:
        stats = generate_statistics(df)
        print(stats["summary"])
    
    insights = generate_insights(df)

    print("\n========== INSIGHTS ==========")

    if insights:

        if "total_revenue" in insights:
            print(f"Total Revenue : ₹{insights['total_revenue']}")

        if "top_product" in insights:
            print(f"Top Product   : {insights['top_product']}")

        if "average_price" in insights:
            print(f"Average Price : ₹{insights['average_price']:.2f}")

        if "revenue_by_product" in insights:
            print("\nRevenue By Product")
            print(insights["revenue_by_product"])

    else:
        print("No business insights available for this dataset.")
        
    trends = trend_analysis(df)

    print("\n========== TRENDS ==========")

    for column, values in trends.items():

        print(f"\n{column}")

        print("Moving Average")

        print(values["moving_average"])

        print("\nGrowth Rate (%)")

        print(values["growth_rate"])
    
    anomalies = detect_anomalies(df)

    print("\n========== ANOMALIES ==========")

    for column, methods in anomalies.items():

        print(f"\n{column}")

        print("\nZ Score")

        print(methods["z_score"])

        print("\nIQR")

        print(methods["iqr"])
    

    generate_charts(df, config["charts"])

    generate_html(df, config,insights)

    generate_pdf(df, config)

@app.command()
def schedule(file: str, template: str, minutes: int = 1):

    def job():

        df = load_data(file)

        config = load_template(template)

        if config["include_statistics"]:
            stats = generate_statistics(df)
            print(stats["summary"])

        generate_charts(df, config["charts"])
        generate_html(df, config)
        generate_pdf(df, config)

        print("Scheduled Report Generated!")

    start_scheduler(job, minutes)

@app.command()
def validate(file: str, table: str = None):
    try:
        df = load_data(file, table)

        print("✅ Dataset loaded successfully!")
        print(f"Rows    : {df.shape[0]}")
        print(f"Columns : {df.shape[1]}")
        print(df.columns.tolist())

    except Exception as e:
        print(f"❌ Validation Failed: {e}")

@app.command()
def list_templates():
    templates_dir = Path("../templates")

    yaml_files = list(templates_dir.glob("*.yaml"))

    if not yaml_files:
        print("No templates found.")
        return

    print("\nAvailable Templates:\n")

    for file in yaml_files:
        print(f"• {file.name}")

if __name__=="__main__":
    app()