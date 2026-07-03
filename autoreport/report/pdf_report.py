from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Table,
    TableStyle,
    Spacer
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch

from datetime import datetime

import os


def generate_pdf(df, config):

    os.makedirs("../reports", exist_ok=True)

    pdf = SimpleDocTemplate(
        "../reports/report.pdf"
    )

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    title_style.alignment = TA_CENTER

    heading_style = styles["Heading2"]

    normal = styles["BodyText"]

    elements = []

    # ===========================
    # TITLE
    # ===========================

    elements.append(
        Paragraph(
            "📊 AutoReport",
            title_style
        )
    )

    elements.append(
        Paragraph(
            "<b>Automated Report & Analytics Generator</b>",
            normal
        )
    )

    elements.append(Spacer(1, 0.25 * inch))

    # ===========================
    # REPORT INFO
    # ===========================

    info = [
        ["Report", config["title"]],
        ["Author", config["author"]],
        ["Generated", datetime.now().strftime("%d %B %Y %I:%M %p")]
    ]

    info_table = Table(info, colWidths=[120, 280])

    info_table.setStyle(

        TableStyle([

            ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#2563EB")),

            ("TEXTCOLOR", (0,0), (-1,0), colors.white),

            ("GRID", (0,0), (-1,-1), 1, colors.grey),

            ("BACKGROUND", (0,1), (-1,-1), colors.whitesmoke),

            ("FONTNAME",(0,0),(-1,-1),"Helvetica-Bold"),

            ("BOTTOMPADDING",(0,0),(-1,-1),10),

            ("TOPPADDING",(0,0),(-1,-1),10),

        ])
    )

    elements.append(info_table)

    elements.append(Spacer(1,0.3*inch))

    # ===========================
    # DATASET SUMMARY
    # ===========================

    summary = [

        ["Rows", len(df)],

        ["Columns", len(df.columns)],

        ["Missing Values", int(df.isnull().sum().sum())],

        ["Duplicate Rows", int(df.duplicated().sum())]

    ]

    elements.append(
        Paragraph(
            "<b>Dataset Summary</b>",
            heading_style
        )
    )

    summary_table = Table(summary,colWidths=[180,120])

    summary_table.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(-1,-1),colors.beige),

            ("GRID",(0,0),(-1,-1),1,colors.black),

            ("FONTNAME",(0,0),(-1,-1),"Helvetica"),

            ("BOTTOMPADDING",(0,0),(-1,-1),8),

            ("TOPPADDING",(0,0),(-1,-1),8),

        ])

    )

    elements.append(summary_table)

    elements.append(Spacer(1,0.3*inch))

    # ===========================
    # DATASET PREVIEW
    # ===========================

    elements.append(

        Paragraph(

            "<b>Dataset Preview</b>",

            heading_style

        )

    )

    preview = [df.columns.tolist()] + df.head(10).values.tolist()

    preview_table = Table(preview)

    preview_table.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#2563EB")),

            ("TEXTCOLOR",(0,0),(-1,0),colors.white),

            ("GRID",(0,0),(-1,-1),1,colors.grey),

            ("BACKGROUND",(0,1),(-1,-1),colors.whitesmoke),

            ("BOTTOMPADDING",(0,0),(-1,-1),8),

            ("TOPPADDING",(0,0),(-1,-1),8),

            ("ALIGN",(0,0),(-1,-1),"CENTER"),

        ])

    )

    elements.append(preview_table)

    elements.append(Spacer(1,0.4*inch))

    # ===========================
    # FOOTER
    # ===========================

    elements.append(

        Paragraph(

            "<br/><br/><font color='grey'>Generated using AutoReport</font>",

            styles["Italic"]

        )

    )

    pdf.build(elements)

    print("PDF Report Generated Successfully!")