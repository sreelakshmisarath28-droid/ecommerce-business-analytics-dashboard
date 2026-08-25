import sqlite3
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH  = os.path.join(BASE_DIR, 'ecommerce.db')

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    return conn

def kpi_summary():
    conn = get_conn()
    df = pd.read_sql_query("""
        SELECT
            COUNT(ORDER_ID)                                         AS Total_Orders,
            COUNT(DISTINCT CUSTOMER_ID)                            AS Unique_Customers,
            ROUND(SUM(TOTAL_AMOUNT), 2)                            AS Total_Revenue,
            ROUND(AVG(TOTAL_AMOUNT), 2)                            AS Avg_Order_Value,
            ROUND(100.0 * SUM(CASE WHEN STATUS='Returned'  THEN 1 ELSE 0 END) / COUNT(*), 1) AS Return_Rate_Pct,
            ROUND(100.0 * SUM(CASE WHEN STATUS='Cancelled' THEN 1 ELSE 0 END) / COUNT(*), 1) AS Cancel_Rate_Pct,
            ROUND(100.0 * SUM(CASE WHEN STATUS='Completed' THEN 1 ELSE 0 END) / COUNT(*), 1) AS Completion_Rate_Pct
        FROM Orders
    """, conn)
    conn.close()
    return df

def revenue_by_category():
    conn = get_conn()
    df = pd.read_sql_query("""
        SELECT CATEGORY,
               ROUND(SUM(TOTAL_AMOUNT), 2)  AS Revenue,
               COUNT(ORDER_ID)              AS Orders,
               ROUND(AVG(TOTAL_AMOUNT), 2)  AS Avg_Order_Value
        FROM Orders
        WHERE STATUS = 'Completed'
        GROUP BY CATEGORY
        ORDER BY Revenue DESC
    """, conn)
    conn.close()
    return df

def top_products():
    conn = get_conn()
    df = pd.read_sql_query("""
        SELECT PRODUCT_NAME, CATEGORY,
               ROUND(SUM(TOTAL_AMOUNT), 2) AS Revenue,
               SUM(QUANTITY)               AS Units_Sold,
               COUNT(ORDER_ID)             AS Orders
        FROM Orders
        WHERE STATUS = 'Completed'
        GROUP BY PRODUCT_NAME, CATEGORY
        ORDER BY Revenue DESC
        LIMIT 10
    """, conn)
    conn.close()
    return df

def monthly_revenue():
    conn = get_conn()
    df = pd.read_sql_query("""
        SELECT SUBSTR(ORDER_DATE, 1, 7)    AS Month,
               ROUND(SUM(TOTAL_AMOUNT), 2) AS Revenue,
               COUNT(ORDER_ID)             AS Orders
        FROM Orders
        WHERE STATUS = 'Completed'
        GROUP BY Month
        ORDER BY Month
    """, conn)
    conn.close()
    return df

def revenue_by_region():
    conn = get_conn()
    df = pd.read_sql_query("""
        SELECT REGION,
               ROUND(SUM(TOTAL_AMOUNT), 2) AS Revenue,
               COUNT(ORDER_ID)             AS Orders
        FROM Orders
        WHERE STATUS = 'Completed'
        GROUP BY REGION
        ORDER BY Revenue DESC
    """, conn)
    conn.close()
    return df

def revenue_by_channel():
    conn = get_conn()
    df = pd.read_sql_query("""
        SELECT CHANNEL,
               ROUND(SUM(TOTAL_AMOUNT), 2) AS Revenue,
               COUNT(ORDER_ID)             AS Orders
        FROM Orders
        WHERE STATUS = 'Completed'
        GROUP BY CHANNEL
        ORDER BY Revenue DESC
    """, conn)
    conn.close()
    return df

def order_status_breakdown():
    conn = get_conn()
    df = pd.read_sql_query("""
        SELECT STATUS, COUNT(ORDER_ID) AS Count
        FROM Orders
        GROUP BY STATUS
        ORDER BY Count DESC
    """, conn)
    conn.close()
    return df

if __name__ == '__main__':
    print("=== KPI SUMMARY ===")
    print(kpi_summary().to_string(index=False))
    print("\n=== REVENUE BY CATEGORY ===")
    print(revenue_by_category().to_string(index=False))
    print("\n=== TOP 10 PRODUCTS ===")
    print(top_products().to_string(index=False))
