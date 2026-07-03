from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import os


def generate_html(df, config, insights=None):

    env = Environment(
        loader=FileSystemLoader("../templates")
    )

    template = env.get_template("reports.html")

    rows = len(df)

    columns = len(df.columns)

    missing = int(df.isnull().sum().sum())

    duplicates = int(df.duplicated().sum())

    numeric_columns = len(df.select_dtypes(include="number").columns)

    generated_on = datetime.now().strftime("%d %B %Y | %I:%M %p")

    html = template.render(

        title=config["title"],

        author=config["author"],

        table=df.to_html(
            index=False,
            classes="table table-striped table-hover",
            border=0
        ),

        rows=rows,

        columns=columns,

        missing=missing,

        duplicates=duplicates,

        numeric_columns=numeric_columns,

        generated_on=generated_on,

        insights=insights if insights else {}
    )

    os.makedirs("../reports", exist_ok=True)

    with open("../reports/report.html", "w", encoding="utf-8") as f:

        f.write(html)

    print("HTML Report Generated Successfully!")