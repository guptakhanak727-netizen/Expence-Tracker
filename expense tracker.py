expenses = []
print("welcome to Expense Tracker")
while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        amount = float(input("Enter expense amount: "))
        description = input("Enter expense description: ")
        expenses.append({"amount": amount, "description": description})
        print("Expense added successfully!")
        
    elif choice == '2':
        if not expenses:
            print("No expenses recorded.")
        else:
            for i, expense in enumerate(expenses):
                print(f"{i + 1}. Amount: {expense['amount']}, Description: {expense['description']}")
                
    elif choice == '3':
        print("Exiting Expense Tracker. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please try again.")