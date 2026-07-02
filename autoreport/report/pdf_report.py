from reportlab.platypus import SimpleDocTemplate, Paragraph, Table
from reportlab.lib.styles import getSampleStyleSheet
import os


def generate_pdf(df,config):

    os.makedirs("reports", exist_ok=True)

    pdf = SimpleDocTemplate("../reports/report.pdf")

    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph(f"Author : {config['author']}", styles["Normal"]))

    elements.append(Paragraph("<br/>Dataset Preview<br/><br/>", styles["Heading2"]))

    data = [df.columns.tolist()] + df.values.tolist()

    table = Table(data)

    elements.append(table)

    pdf.build(elements)

    print("PDF Report Generated Successfully!")