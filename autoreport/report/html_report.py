from jinja2 import Environment, FileSystemLoader
import os


def generate_html(df):
    env = Environment(loader=FileSystemLoader("../templates"))
    template = env.get_template("reports.html")

    html = template.render(
        table=df.to_html(index=False)
    )

    os.makedirs("reports", exist_ok=True)

    with open("reports/report.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("HTML Report Generated!")