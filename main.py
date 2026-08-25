"""
E-Commerce Business Analytics Dashboard
========================================
Author  : Sreelakshmi Suresh
Tools   : Python, SQL, SQLite, Pandas, Matplotlib, ReportLab
GitHub  : github.com/sreelakshmisarath28-droid
"""

from generate_data  import generate_data
from analysis       import kpi_summary, revenue_by_category, top_products
from dashboard      import make_dashboard
from generate_report import generate_report

def main():
    print("=" * 55)
    print("  E-COMMERCE BUSINESS ANALYTICS DASHBOARD")
    print("=" * 55)

    print("\n[1/4] Generating sample e-commerce data...")
    generate_data()

    print("\n[2/4] Running KPI analysis queries...")
    kpi  = kpi_summary().iloc[0]
    print(f"      Total Revenue    : EUR {kpi['Total_Revenue']:,.2f}")
    print(f"      Total Orders     : {kpi['Total_Orders']:,}")
    print(f"      Unique Customers : {kpi['Unique_Customers']:,}")
    print(f"      Avg Order Value  : EUR {kpi['Avg_Order_Value']:,.2f}")
    print(f"      Completion Rate  : {kpi['Completion_Rate_Pct']}%")
    print(f"      Return Rate      : {kpi['Return_Rate_Pct']}%")

    print("\n[3/4] Generating Power BI style dashboard...")
    dash_path = make_dashboard()
    print(f"      Saved: {dash_path}")

    print("\n[4/4] Generating PDF stakeholder report...")
    pdf_path = generate_report()
    print(f"      Saved: {pdf_path}")

    print("\n" + "=" * 55)
    print("  ALL DONE! Check the reports/ folder.")
    print("=" * 55)

if __name__ == '__main__':
    main()
