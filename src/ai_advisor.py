import sqlite3
import pandas as pd
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_response(data_summary,instruction):
    
    response=client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"system","content":"You are a financial advisor. Give very short, direct answer (max 2-3 bullet points), Every thing in Rupees "},
            {"role":"user","content":f"Here is my spending:\n {data_summary}\n{instruction}"}
        ]
    )

    return response.choices[0].message.content

def get_financial_advice(summary):
    return get_response(summary, "Give 3 very short actionable financial tips.")


def get_overspending_advice(summary):
    return get_response(summary, "Which category has overspending? Explain briefly.")


def get_budget_suggestion(summary):
    return get_response(summary, "Suggest a simple monthly budget in 3 short points.")



