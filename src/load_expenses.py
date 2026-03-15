import pandas as pd

df=pd.read_csv(r"D:\my_git\ai_expense_analyzer\data\expenses.csv")

print("Dataset Preview:")
print(df.head(5))


print("\nColumns:")
print(df.columns)

print("\nTotal Spending:")
print(df["amount"].sum())

