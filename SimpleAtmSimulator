class InsufficientFundsError(Exception):
    pass

balance = 5000  # Initial balance


while True:
    print("\n=== ATM Menu ===")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    try:
        choice = int(input("Choose an option (1-4): "))
        
        if choice == 1:
            print(f"Your balance is: ₦{balance}")
        
        elif choice == 2:
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                raise ValueError("Amount must be positive.")
            balance += amount
            print(f"₦{amount} deposited. New balance: ₦{balance}")
        
        elif choice == 3:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                raise ValueError("Amount must be positive.")
            if amount > balance:
                raise InsufficientFundsError("Insufficient balance.")
            balance -= amount
            print(f"₦{amount} withdrawn. New balance: ₦{balance}")
        
        elif choice == 4:
            print("Thank you for using the ATM.")
            break
        
        else:
            print("Invalid choice. Choose from 1 to 4.")

    except ValueError as ve:
        print("Input error:", ve)

    except InsufficientFundsError as ie:
        print("Transaction error:", ie)

    except KeyboardInterrupt:
        print("\nSession cancelled by user.")
        break

    finally:
        print("Transaction complete.\n")
