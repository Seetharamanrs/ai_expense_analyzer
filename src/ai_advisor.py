import sqlite3
import pandas as pd
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

conn= sqlite3.connect("../expenses.db")

query="""
SELECT category, SUM(amount) as total
FROM expenses
GROUP BY category
"""

df=pd.read_sql(query,conn)


conn.close()

data_summary=df.to_string(index=False)

print("Expenses Summary\n", data_summary)
    
response=client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role":"system","content":"You are a financial advisor. "},
        {"role":"user","content":f"Here is my spending:\n {data_summary}\n Give 3 short actionable financial tips in bullet points."}
    ]
)

print("\nAI Advice:\n")
print(response.choices[0].message.content)

