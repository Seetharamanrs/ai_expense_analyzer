import sqlite3
import pandas as pd 


def total_spending():
    conn= sqlite3.connect("../expenses.db")
    query="SELECT SUM(amount) as total_spending FROM expenses"
    total=pd.read_sql(query,conn)
    conn.close()
    return total

def get_category_spending():
    conn= sqlite3.connect("../expenses.db")
    query2 = """
    SELECT category, SUM(amount) as total
    FROM expenses
    GROUP BY category
    """
    category_spend=pd.read_sql(query2,conn)
    conn.close()
    return category_spend

def get_highest_expense_category():
    import sqlite3
    import pandas as pd

    conn = sqlite3.connect("../expenses.db")

    query = """
    SELECT category, SUM(amount) as total
    FROM expenses
    GROUP BY category
    ORDER BY total DESC
    LIMIT 1
    """

    df = pd.read_sql(query, conn)
    conn.close()

    return df
def get_monthly_trend():
    import sqlite3
    import pandas as pd

    conn = sqlite3.connect("../expenses.db")

    query = """
    SELECT 
        strftime('%Y-%m', date) AS month,
        category,
        SUM(amount) AS total
    FROM expenses
    GROUP BY month, category
    ORDER BY month
    """

    df = pd.read_sql(query, conn)
    conn.close()

    return df