class InvalidAmountError(Exception): pass
class EmptyFieldError(Exception): pass

expenses = []

def add_expense(amount, description, category):
    if not description.strip() or not category.strip():
        raise EmptyFieldError("Description and category cannot be empty.")
    
    try:
        amount = float(amount)
    except ValueError:
        raise InvalidAmountError("Amount must be a number.")

    if amount <= 0:
        raise InvalidAmountError("Amount must be greater than 0.")

    expenses.append({
        "amount": amount,
        "description": description.strip(),
        "category": category.strip().capitalize()
    })
    print("✅ Expense added successfully.")

def show_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    total = 0
    print("\n📄 All Expenses:")
    print("-" * 40)
    for idx, exp in enumerate(expenses, 1):
        print(f"{idx}. ₦{exp['amount']:.2f} - {exp['description']} ({exp['category']})")
        total += exp["amount"]
    print("-" * 40)
    print(f"💰 Total Spent: ₦{total:.2f}")

while True:
    try:
        print("\n=== Daily Expense Tracker ===")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            amt = input("Enter amount: ₦")
            desc = input("What was it spent on? ")
            cat = input("Enter category (e.g. food, transport): ")
            add_expense(amt, desc, cat)

        elif choice == '2':
            show_expenses()

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Choose 1–3.")

    except (InvalidAmountError, EmptyFieldError) as e:
        print("❌ Error:", e)

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        break

    finally:
        print("Action completed.\n")
