import typer
import pandas as pd
from analysis.statistics import generate_statistics
from charts.chart_factory import generate_charts
from report.html_report import generate_html
app=typer.Typer()
@app.command()
def hello():
    print("Welcome to Auto Report")
    
@app.command()
def generate(file: str):
    df = pd.read_csv(file)

    stats = generate_statistics(df)

    print(stats["summary"])
    generate_charts(df)
    generate_html(df)

if __name__=="__main__":
    app()