# 📊 AutoReport – Automated Report & Analytics Generator

A Python-based Command Line Interface (CLI) application that automates data analysis and generates professional HTML and PDF reports from multiple data sources including CSV, Excel, JSON, and SQLite.

---

## 🚀 Features

- 📂 Supports multiple data sources
  - CSV
  - Excel (.xlsx)
  - JSON
  - SQLite

- 📈 Data Analytics
  - Statistical Summary
  - Missing Value Detection
  - Duplicate Detection
  - Dataset Information

- 📊 Automatic Chart Generation
  - Bar Chart
  - Line Chart
  - Pie Chart
  - Scatter Plot

- 📄 Report Generation
  - HTML Report
  - PDF Report

- ⚙️ YAML Configuration
  - Report Title
  - Author
  - Charts to Generate
  - Enable/Disable Statistics

- ⏰ Scheduled Report Generation using APScheduler

- 🧪 Unit Testing with Pytest

---

# 📁 Project Structure

```text
AutoReport2
│
├── autoreport
│   ├── analysis
│   ├── charts
│   ├── ingestion
│   ├── report
│   ├── scheduler
│   ├── utils
│   └── main.py
│
├── data
│
├── reports
│
├── templates
│
├── tests
│
├── requirements.txt
├── pyproject.toml
└── .gitignore
```

---

# 🛠️ Technologies Used

- Python 3.11+
- Pandas
- Matplotlib
- Jinja2
- ReportLab
- PyYAML
- APScheduler
- SQLite3
- Typer
- Pytest

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/ashu2506-py/AutoReport-Automated-Report-Analytics-Generator.git
```

Move inside the project

```bash
cd AutoReport2
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Usage

Generate report from CSV

```bash
python autoreport/main.py generate data/sales.csv templates/sales.yaml
```

Generate report from SQLite

```bash
python autoreport/main.py generate data/sales.db templates/sales.yaml --table sales
```

Run Scheduled Reports

```bash
python autoreport/main.py schedule data/sales.csv templates/sales.yaml --minutes 2
```

---

# 📂 Output

The application automatically generates:

```text
reports/
│
├── report.html
├── report.pdf
└── charts/
    ├── bar_chart.png
    ├── line_chart.png
    ├── pie_chart.png
    └── scatter_chart.png
```

---

# 🧪 Run Tests

```bash
pytest
```

---

# 🎯 Future Improvements

- REST API Data Source
- Interactive Dashboard
- Email Report Delivery
- Dark Theme Reports
- AI-powered Insights
- Docker Support

---

# 👨‍💻 Author

**Ashutosh Singh**

GitHub: https://github.com/ashu2506-py

---

## ⭐ If you found this project useful, consider giving it a star!