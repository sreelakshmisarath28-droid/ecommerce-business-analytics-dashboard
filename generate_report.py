from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.units import inch
from datetime import datetime
import os
from analysis import (kpi_summary, revenue_by_category,
                      top_products, monthly_revenue, revenue_by_channel)

BASE_DIR    = os.path.dirname(os.path.abspath(__file__))
REPORTS_DIR = os.path.join(BASE_DIR, 'reports')
BLUE        = colors.HexColor('#1565C0')
LIGHTBLUE   = colors.HexColor('#E3F2FD')
WHITE       = colors.white

def generate_report():
    os.makedirs(REPORTS_DIR, exist_ok=True)
    path = os.path.join(REPORTS_DIR, 'ecommerce_report.pdf')
    doc  = SimpleDocTemplate(path, pagesize=A4,
                             rightMargin=40, leftMargin=40,
                             topMargin=40, bottomMargin=40)
    styles = getSampleStyleSheet()
    elements = []

    title_style = ParagraphStyle('Title', parent=styles['Title'],
                                  fontSize=22, textColor=BLUE,
                                  spaceAfter=4, alignment=1)
    sub_style   = ParagraphStyle('Sub', parent=styles['Normal'],
                                  fontSize=11, textColor=colors.HexColor('#1E88E5'),
                                  spaceAfter=2, alignment=1)
    head_style  = ParagraphStyle('Head', parent=styles['Heading2'],
                                  fontSize=14, textColor=BLUE, spaceAfter=6)
    date_style  = ParagraphStyle('Date', parent=styles['Normal'],
                                  fontSize=9, textColor=colors.grey, alignment=1)

    elements.append(Paragraph("E-Commerce Business Analytics Report", title_style))
    elements.append(Paragraph("KPI Dashboard | 2024 Annual Summary", sub_style))
    elements.append(Paragraph(f"Prepared by: Sreelakshmi Suresh | Generated: {datetime.now().strftime('%d %B %Y')}", date_style))
    elements.append(Spacer(1, 0.2*inch))

    # Dashboard image
    img_path = os.path.join(REPORTS_DIR, 'ecommerce_dashboard.png')
    if os.path.exists(img_path):
        elements.append(Image(img_path, width=7*inch, height=9*inch))
        elements.append(Spacer(1, 0.2*inch))

    # KPI Summary Table
    elements.append(Paragraph("Executive KPI Summary", head_style))
    kpi = kpi_summary().iloc[0]
    kpi_table_data = [
        ['KPI Metric', 'Value'],
        ['Total Revenue', f"€{kpi['Total_Revenue']:,.2f}"],
        ['Total Orders', f"{kpi['Total_Orders']:,}"],
        ['Unique Customers', f"{kpi['Unique_Customers']:,}"],
        ['Average Order Value', f"€{kpi['Avg_Order_Value']:,.2f}"],
        ['Order Completion Rate', f"{kpi['Completion_Rate_Pct']}%"],
        ['Return Rate', f"{kpi['Return_Rate_Pct']}%"],
        ['Cancellation Rate', f"{kpi['Cancel_Rate_Pct']}%"],
    ]
    t = Table(kpi_table_data, colWidths=[3.5*inch, 3*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (-1,0),  BLUE),
        ('TEXTCOLOR',     (0,0), (-1,0),  WHITE),
        ('FONTNAME',      (0,0), (-1,0),  'Helvetica-Bold'),
        ('FONTSIZE',      (0,0), (-1,-1), 10),
        ('ALIGN',         (0,0), (-1,-1), 'CENTER'),
        ('ROWBACKGROUNDS',(0,1), (-1,-1), [LIGHTBLUE, WHITE]),
        ('GRID',          (0,0), (-1,-1), 0.5, colors.HexColor('#90CAF9')),
        ('TOPPADDING',    (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 0.2*inch))

    # Revenue by Category Table
    elements.append(Paragraph("Revenue by Category", head_style))
    cat = revenue_by_category()
    cat_data = [['Category', 'Revenue (EUR)', 'Orders', 'Avg Order Value']]
    for _, row in cat.iterrows():
        cat_data.append([row['CATEGORY'], f"€{row['Revenue']:,.2f}",
                         str(row['Orders']), f"€{row['Avg_Order_Value']:,.2f}"])
    t2 = Table(cat_data, colWidths=[2*inch, 2*inch, 1.5*inch, 2*inch])
    t2.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (-1,0),  BLUE),
        ('TEXTCOLOR',     (0,0), (-1,0),  WHITE),
        ('FONTNAME',      (0,0), (-1,0),  'Helvetica-Bold'),
        ('FONTSIZE',      (0,0), (-1,-1), 9),
        ('ALIGN',         (0,0), (-1,-1), 'CENTER'),
        ('ROWBACKGROUNDS',(0,1), (-1,-1), [LIGHTBLUE, WHITE]),
        ('GRID',          (0,0), (-1,-1), 0.5, colors.HexColor('#90CAF9')),
        ('TOPPADDING',    (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    elements.append(t2)
    elements.append(Spacer(1, 0.2*inch))

    # Top 10 Products Table
    elements.append(Paragraph("Top 10 Products by Revenue", head_style))
    prod = top_products()
    prod_data = [['#', 'Product', 'Category', 'Revenue (EUR)', 'Units Sold']]
    for i, (_, row) in enumerate(prod.iterrows(), 1):
        prod_data.append([str(i), row['PRODUCT_NAME'], row['CATEGORY'],
                          f"€{row['Revenue']:,.2f}", str(row['Units_Sold'])])
    t3 = Table(prod_data, colWidths=[0.4*inch, 2.4*inch, 1.5*inch, 1.7*inch, 1.2*inch])
    t3.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (-1,0),  BLUE),
        ('TEXTCOLOR',     (0,0), (-1,0),  WHITE),
        ('FONTNAME',      (0,0), (-1,0),  'Helvetica-Bold'),
        ('FONTSIZE',      (0,0), (-1,-1), 9),
        ('ALIGN',         (0,0), (-1,-1), 'CENTER'),
        ('ROWBACKGROUNDS',(0,1), (-1,-1), [LIGHTBLUE, WHITE]),
        ('GRID',          (0,0), (-1,-1), 0.5, colors.HexColor('#90CAF9')),
        ('TOPPADDING',    (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    elements.append(t3)
    elements.append(Spacer(1, 0.15*inch))
    elements.append(Paragraph("--- End of Report ---",
                               ParagraphStyle('End', parent=styles['Normal'],
                                              fontSize=9, textColor=colors.grey, alignment=1)))
    doc.build(elements)
    print(f"PDF Report saved: {path}")
    return path

if __name__ == '__main__':
    generate_report()
