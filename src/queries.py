import sqlite3
import pandas as pd 

conn= sqlite3.connect("../expenses.db")

query1="SELECT SUM(amount) as total_spending FROM expenses"
total=pd.read_sql(query1,conn)

print("Total Spending")
print(total)




query2 = """
SELECT category, SUM(amount) as total
FROM expenses
GROUP BY category
"""


category_spend=pd.read_sql(query2,conn)

print("\n Spending by Category")
print(category_spend)
conn.close()


