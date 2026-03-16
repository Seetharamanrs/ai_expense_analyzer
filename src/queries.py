import sqlite3
import pandas as pd 

conn= sqlite3.connect("../expenses.db")

query1="SELECT SUM(amount) as total_spending FROM expenses"
total=pd.read_sql(query1,conn)

print("Total Spending")
print(total)



