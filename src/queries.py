import sqlite3
import pandas as pd 


def total_spending():
    conn= sqlite3.connect("../expenses.db")
    query="SELECT SUM(amount) as total_spending FROM expenses"
    total=pd.read_sql(query,conn)
    conn.close()
    return total

def total_spending():
    conn= sqlite3.connect("../expenses.db")
    query2 = """
    SELECT category, SUM(amount) as total
    FROM expenses
    GROUP BY category
    """
    category_spend=pd.read_sql(query2,conn)
    conn.close()
    return category_spend


