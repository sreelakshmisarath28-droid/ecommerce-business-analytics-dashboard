import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec
import pandas as pd
import os
from analysis import (kpi_summary, revenue_by_category, top_products,
                      monthly_revenue, revenue_by_region,
                      revenue_by_channel, order_status_breakdown)

BASE_DIR    = os.path.dirname(os.path.abspath(__file__))
REPORTS_DIR = os.path.join(BASE_DIR, 'reports')
os.makedirs(REPORTS_DIR, exist_ok=True)

# ---- Colour palette (Blue & White professional) ----
PRIMARY   = '#1565C0'
SECONDARY = '#1E88E5'
LIGHT     = '#90CAF9'
ACCENT    = '#0D47A1'
BG        = '#F5F8FF'
WHITE     = '#FFFFFF'
GRAY      = '#78909C'
COLORS    = ['#1565C0','#1E88E5','#42A5F5','#90CAF9','#0D47A1','#2196F3','#64B5F6']

def make_dashboard():
    kpi   = kpi_summary().iloc[0]
    cat   = revenue_by_category()
    prod  = top_products()
    mrev  = monthly_revenue()
    reg   = revenue_by_region()
    chan  = revenue_by_channel()
    stat  = order_status_breakdown()

    fig = plt.figure(figsize=(22, 28), facecolor=BG)
    fig.suptitle('E-Commerce Business Analytics Dashboard',
                 fontsize=26, fontweight='bold', color=ACCENT, y=0.98)
    fig.text(0.5, 0.965, 'KPI Report | 2024 | Prepared by: Sreelakshmi Suresh | Tools: Python, SQL, Matplotlib',
             ha='center', fontsize=11, color=GRAY)

    gs = GridSpec(5, 3, figure=fig,
                  hspace=0.55, wspace=0.35,
                  top=0.95, bottom=0.03, left=0.05, right=0.97)

    # ---- KPI Cards ----
    kpi_data = [
        ('Total Revenue',      f"€{kpi['Total_Revenue']:,.0f}",    '💰'),
        ('Total Orders',       f"{kpi['Total_Orders']:,}",          '📦'),
        ('Unique Customers',   f"{kpi['Unique_Customers']:,}",      '👥'),
        ('Avg Order Value',    f"€{kpi['Avg_Order_Value']:,.2f}",   '🛒'),
        ('Completion Rate',    f"{kpi['Completion_Rate_Pct']}%",    '✅'),
        ('Return Rate',        f"{kpi['Return_Rate_Pct']}%",        '↩️'),
    ]
    for i, (label, value, icon) in enumerate(kpi_data):
        ax = fig.add_subplot(gs[0, i % 3] if i < 3 else gs[1, i % 3])
        ax.set_facecolor(PRIMARY if i < 3 else SECONDARY)
        ax.set_xticks([]); ax.set_yticks([])
        for spine in ax.spines.values(): spine.set_visible(False)
        ax.text(0.5, 0.65, value, ha='center', va='center',
                fontsize=22, fontweight='bold', color=WHITE,
                transform=ax.transAxes)
        ax.text(0.5, 0.25, label, ha='center', va='center',
                fontsize=11, color=WHITE, transform=ax.transAxes)

    # ---- Monthly Revenue Trend ----
    ax1 = fig.add_subplot(gs[2, :2])
    ax1.set_facecolor(WHITE)
    ax1.plot(mrev['Month'], mrev['Revenue'], color=PRIMARY,
             linewidth=2.5, marker='o', markersize=7, markerfacecolor=ACCENT)
    ax1.fill_between(range(len(mrev)), mrev['Revenue'],
                     alpha=0.15, color=SECONDARY)
    ax1.set_xticks(range(len(mrev)))
    ax1.set_xticklabels(mrev['Month'], rotation=45, ha='right', fontsize=9)
    ax1.set_title('Monthly Revenue Trend (EUR)', fontsize=13,
                  fontweight='bold', color=ACCENT, pad=10)
    ax1.set_ylabel('Revenue (EUR)', fontsize=10, color=GRAY)
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'€{x:,.0f}'))
    ax1.grid(axis='y', linestyle='--', alpha=0.4)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)

    # ---- Order Status Pie ----
    ax2 = fig.add_subplot(gs[2, 2])
    ax2.set_facecolor(WHITE)
    pie_colors = [PRIMARY, LIGHT, GRAY]
    wedges, texts, autotexts = ax2.pie(
        stat['Count'], labels=stat['STATUS'],
        autopct='%1.1f%%', colors=pie_colors,
        startangle=90, pctdistance=0.75,
        textprops={'fontsize': 9})
    for at in autotexts: at.set_color(WHITE); at.set_fontweight('bold')
    ax2.set_title('Order Status Breakdown', fontsize=13,
                  fontweight='bold', color=ACCENT, pad=10)

    # ---- Revenue by Category Bar ----
    ax3 = fig.add_subplot(gs[3, :2])
    ax3.set_facecolor(WHITE)
    bars = ax3.barh(cat['CATEGORY'], cat['Revenue'],
                    color=COLORS[:len(cat)], edgecolor='white', height=0.6)
    for bar, val in zip(bars, cat['Revenue']):
        ax3.text(bar.get_width() + 500, bar.get_y() + bar.get_height()/2,
                 f'€{val:,.0f}', va='center', fontsize=9, color=ACCENT)
    ax3.set_title('Revenue by Category (EUR)', fontsize=13,
                  fontweight='bold', color=ACCENT, pad=10)
    ax3.set_xlabel('Revenue (EUR)', fontsize=10, color=GRAY)
    ax3.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'€{x:,.0f}'))
    ax3.invert_yaxis()
    ax3.spines['top'].set_visible(False)
    ax3.spines['right'].set_visible(False)
    ax3.grid(axis='x', linestyle='--', alpha=0.4)

    # ---- Revenue by Region ----
    ax4 = fig.add_subplot(gs[3, 2])
    ax4.set_facecolor(WHITE)
    ax4.bar(reg['REGION'], reg['Revenue'],
            color=COLORS[:len(reg)], edgecolor='white', width=0.6)
    ax4.set_title('Revenue by Region', fontsize=13,
                  fontweight='bold', color=ACCENT, pad=10)
    ax4.set_ylabel('Revenue (EUR)', fontsize=10, color=GRAY)
    ax4.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'€{x:,.0f}'))
    ax4.tick_params(axis='x', rotation=15)
    ax4.spines['top'].set_visible(False)
    ax4.spines['right'].set_visible(False)
    ax4.grid(axis='y', linestyle='--', alpha=0.4)

    # ---- Top 10 Products ----
    ax5 = fig.add_subplot(gs[4, :])
    ax5.set_facecolor(WHITE)
    prod_short = prod['PRODUCT_NAME'].str[:25]
    bars2 = ax5.bar(range(len(prod)), prod['Revenue'],
                    color=COLORS[:len(prod)] + COLORS, edgecolor='white', width=0.65)
    ax5.set_xticks(range(len(prod)))
    ax5.set_xticklabels(prod_short, rotation=30, ha='right', fontsize=9)
    for bar, val in zip(bars2, prod['Revenue']):
        ax5.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 200,
                 f'€{val:,.0f}', ha='center', fontsize=8, color=ACCENT, fontweight='bold')
    ax5.set_title('Top 10 Products by Revenue (EUR)', fontsize=13,
                  fontweight='bold', color=ACCENT, pad=10)
    ax5.set_ylabel('Revenue (EUR)', fontsize=10, color=GRAY)
    ax5.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'€{x:,.0f}'))
    ax5.spines['top'].set_visible(False)
    ax5.spines['right'].set_visible(False)
    ax5.grid(axis='y', linestyle='--', alpha=0.4)

    path = os.path.join(REPORTS_DIR, 'ecommerce_dashboard.png')
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=BG)
    plt.close()
    print(f"Dashboard saved: {path}")
    return path

if __name__ == '__main__':
    make_dashboard()
