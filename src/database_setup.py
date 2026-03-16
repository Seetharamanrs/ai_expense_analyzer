import pandas as pd 
import sqlite3

df=pd.read_csv(r"D:\my_git\ai_expense_analyzer\data\expenses.csv")

conn=sqlite3.connect("../expenses.db")

df.to_sql("expenses",conn,if_exists="replace",index=False)

print("Data sucessfully stored in SQLite database! ")

conn.close()












