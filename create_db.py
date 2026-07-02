import sqlite3

conn = sqlite3.connect("../data/sales.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales(
    Product TEXT,
    Quantity INTEGER,
    Price INTEGER
)
""")

cursor.execute("DELETE FROM sales")

cursor.executemany(
    "INSERT INTO sales VALUES (?, ?, ?)",
    [
        ("Laptop", 5, 55000),
        ("Mouse", 20, 500),
        ("Keyboard", 10, 1200),
        ("Monitor", 7, 15000),
        ("Headphones", 15, 2500)
    ]
)

conn.commit()
conn.close()

print("Database Created Successfully!")