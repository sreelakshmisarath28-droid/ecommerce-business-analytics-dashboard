# 🛒 E-Commerce Business Analytics Dashboard

A Business Analyst portfolio project built with **Python, SQL, SQLite, Pandas, and Matplotlib** to analyse e-commerce sales data and generate Power BI style KPI dashboards and stakeholder PDF reports.

---

## Features

- Generates 2,000 realistic e-commerce order records using Python
- Stores and queries data using SQLite and SQL
- Calculates 7 key business KPIs using SQL queries
- Produces a professional Power BI style multi-chart dashboard (PNG)
- Generates a complete stakeholder PDF report with tables and charts
- Blue and White professional theme throughout

---

## KPIs Tracked

| KPI | Description |
|---|---|
| Total Revenue | Sum of all completed order values |
| Total Orders | Count of all orders placed |
| Unique Customers | Number of distinct customers |
| Average Order Value | Mean revenue per completed order |
| Order Completion Rate | Percentage of successfully completed orders |
| Return Rate | Percentage of returned orders |
| Cancellation Rate | Percentage of cancelled orders |

---

## Dashboard Charts

- Monthly Revenue Trend (line chart)
- Revenue by Category (horizontal bar chart)
- Revenue by Region (bar chart)
- Top 10 Products by Revenue (bar chart)
- Order Status Breakdown (pie chart)
- KPI Summary Cards

---

## Project Structure

```
ecommerce-business-analytics-dashboard/
│
├── main.py              # Run this to generate everything
├── generate_data.py     # Creates SQLite database with sample data
├── analysis.py          # SQL queries and KPI calculations using Pandas
├── dashboard.py         # Power BI style dashboard generator
├── generate_report.py   # PDF stakeholder report generator
├── requirements.txt     # Python dependencies
├── ecommerce.db         # Auto-created SQLite database
│
└── reports/
    ├── ecommerce_dashboard.png   # Dashboard image
    └── ecommerce_report.pdf      # Full stakeholder PDF report
```

---

## How to Run

### Step 1 -- Install dependencies
```bash
pip install -r requirements.txt
```

### Step 2 -- Run the project
```bash
python main.py
```

### Step 3 -- Check results
Open the `reports/` folder to find:
- `ecommerce_dashboard.png` -- your Power BI style dashboard
- `ecommerce_report.pdf` -- your full stakeholder PDF report

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| SQL / SQLite | Data storage and KPI queries |
| Pandas | Data manipulation and analysis |
| Matplotlib | Dashboard and chart generation |
| ReportLab | PDF report generation |
| Git | Version control |

---

## CV Description

> Developed an end-to-end E-Commerce Business Analytics Dashboard using Python, SQL, and Pandas. Designed a SQLite database schema for 2,000+ order records, wrote SQL queries to calculate 7 business KPIs, and generated a Power BI style multi-chart dashboard and automated PDF stakeholder report using Matplotlib and ReportLab.

## Duration
Feb2026 --- Present | Developer | Business Analyst Project
