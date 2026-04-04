from queries import(
        get_category_spending,
        get_highest_expense_category,
        total_spending,
        get_monthly_trend
)

from ai_advisor import(
    get_financial_advice,
    get_overspending_advice,
    get_budget_suggestion
)
from database_setup import load_csv_to_db
def main():
    load_csv_to_db()
    while True:
        print("\n 1. Total Spending.")
        print("2. Category Breakdown")
        print("3. Highest Expense")
        print("4. Monthly Trend")
        
        print("\n5. AI Financial Advice")
        print("6. AI Overspending Detection")
        print("7. AI Budget Suggestion")

        print("\n8. Exit")

        choice=input("Enter your choice: ")
        if choice=="1":
            print(total_spending())
        elif choice=="2":
            print(get_category_spending())
        elif choice == "3":
            print(get_highest_expense_category())
        elif choice=="4":
            print(get_monthly_trend())

        elif choice in ["5", "6", "7"]:
                category = get_category_spending()
                summary = category.to_string(index=False)

                print("\nExpense Summary:\n", summary)

                if choice == "5":
                    print("\nAI Advice:\n", get_financial_advice(summary))

                elif choice == "6":
                    print("\nOverspending Insight:\n", get_overspending_advice(summary))

                elif choice == "7":
                    print("\nBudget Suggestion:\n", get_budget_suggestion(summary))

        elif choice == "8":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()