import sqlite3
import pandas as pd
import random
from datetime import datetime, timedelta
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'ecommerce.db')

CATEGORIES = ['Electronics', 'Clothing', 'Home & Garden', 'Sports', 'Books', 'Beauty', 'Toys']
PRODUCTS = {
    'Electronics':  ['Laptop Pro X', 'Wireless Headphones', 'Smart Watch', 'Tablet 10"', 'USB-C Hub', 'Bluetooth Speaker'],
    'Clothing':     ['Winter Jacket', 'Running Shoes', 'Casual T-Shirt', 'Denim Jeans', 'Sports Hoodie', 'Formal Shirt'],
    'Home & Garden':['Coffee Maker', 'Air Purifier', 'LED Desk Lamp', 'Plant Pot Set', 'Kitchen Knife Set', 'Wall Clock'],
    'Sports':       ['Yoga Mat', 'Dumbbells Set', 'Cycling Helmet', 'Tennis Racket', 'Protein Shaker', 'Running Belt'],
    'Books':        ['Python for Data Science', 'Business Analytics Guide', 'SQL Mastery', 'Machine Learning A-Z', 'Agile Handbook', 'Power BI Essentials'],
    'Beauty':       ['Face Serum', 'Moisturiser SPF50', 'Hair Oil', 'Lip Balm Set', 'Eye Cream', 'Body Lotion'],
    'Toys':         ['LEGO City Set', 'Board Game Deluxe', 'RC Racing Car', 'Puzzle 1000pc', 'Action Figure Set', 'Art Kit'],
}
PRICES = {
    'Electronics': (49.99, 899.99), 'Clothing': (14.99, 149.99),
    'Home & Garden': (19.99, 249.99), 'Sports': (9.99, 199.99),
    'Books': (9.99, 49.99), 'Beauty': (7.99, 79.99), 'Toys': (12.99, 129.99),
}
REGIONS   = ['North', 'South', 'East', 'West', 'Central']
CHANNELS  = ['Online', 'Mobile App', 'Marketplace']
STATUSES  = ['Completed', 'Completed', 'Completed', 'Returned', 'Cancelled']
CUSTOMERS = [f'CUST{str(i).zfill(4)}' for i in range(1, 301)]

def generate_data():
    conn = sqlite3.connect(DB_PATH)
    cur  = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS Orders")
    cur.execute("""CREATE TABLE Orders (
        ORDER_ID      TEXT PRIMARY KEY,
        ORDER_DATE    TEXT,
        CUSTOMER_ID   TEXT,
        PRODUCT_NAME  TEXT,
        CATEGORY      TEXT,
        UNIT_PRICE    REAL,
        QUANTITY      INTEGER,
        TOTAL_AMOUNT  REAL,
        REGION        TEXT,
        CHANNEL       TEXT,
        STATUS        TEXT
    )""")

    rows = []
    start = datetime(2024, 1, 1)
    for i in range(1, 2001):
        cat      = random.choice(CATEGORIES)
        product  = random.choice(PRODUCTS[cat])
        lo, hi   = PRICES[cat]
        price    = round(random.uniform(lo, hi), 2)
        qty      = random.randint(1, 5)
        date     = start + timedelta(days=random.randint(0, 364))
        status   = random.choice(STATUSES)
        total    = round(price * qty, 2) if status == 'Completed' else 0.0
        rows.append((
            f'ORD{str(i).zfill(5)}',
            date.strftime('%Y-%m-%d'),
            random.choice(CUSTOMERS),
            product, cat, price, qty, total,
            random.choice(REGIONS),
            random.choice(CHANNELS),
            status
        ))

    cur.executemany("""INSERT INTO Orders VALUES(?,?,?,?,?,?,?,?,?,?,?)""", rows)
    conn.commit()
    conn.close()
    print(f"Database created with {len(rows)} orders!")

if __name__ == '__main__':
    generate_data()
