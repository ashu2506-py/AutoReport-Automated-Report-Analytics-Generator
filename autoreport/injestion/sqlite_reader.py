import sqlite3
import pandas as pd


def read_sqlite(database, table):

    conn = sqlite3.connect(database)

    df = pd.read_sql_query(f"SELECT * FROM {table}", conn)

    conn.close()

    return df