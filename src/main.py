from queries import(
        get_category_spending,
        get_highest_expense_category,
        total_spending
)

from ai_advisor import(
    get_financial_advice,
    get_overspending_advice,
    get_budget_suggestion
)
while True:
    print("\n 1. Total Spending.")
    print("2. Category Breakdown")
    print("3. Highest Expense")
    
    print("\n4. AI Financial Advice")
    print("5. AI Overspending Detection")
    print("6. AI Budget Suggestion")

    print("\n7. Exit")

    choice=input("Enter your choice: ")
    if choice=="1":
        print(total_spending())
    elif choice=="2":
        print(get_category_spending())


    elif choice == "3":
            print(get_highest_expense_category())

    elif choice in ["4", "5", "6"]:
            category = get_category_spending()
            summary = category.to_string(index=False)

            print("\nExpense Summary:\n", summary)

            if choice == "4":
                print("\nAI Advice:\n", get_financial_advice(summary))

            elif choice == "5":
                print("\nOverspending Insight:\n", get_overspending_advice(summary))

            elif choice == "6":
                print("\nBudget Suggestion:\n", get_budget_suggestion(summary))

    elif choice == "7":
        break

    else:
        print("Invalid choice")