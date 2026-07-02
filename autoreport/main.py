import typer
import pandas as pd
from analysis.statistics import generate_statistics
from charts.chart_factory import generate_charts
from report.html_report import generate_html
from report.pdf_report import generate_pdf
from report.template_loader import load_template
from injestion.data_loader import load_data
from scheduler.scheduler import start_scheduler
app=typer.Typer()
@app.command()
def hello():
    print("Welcome to Auto Report")
    
@app.command()
def generate(file: str, template: str,table:str=None):

    config = load_template(template)

    df = load_data(file,table)
    

    if config["include_statistics"]:
        stats = generate_statistics(df)
        print(stats["summary"])

    generate_charts(df, config["charts"])

    generate_html(df, config)

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

if __name__=="__main__":
    app()