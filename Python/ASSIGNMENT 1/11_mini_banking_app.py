accounts = []


def create_account():
    name = input("Enter Account Holder Name: ")

    while True:
        account_number = input("Enter Account Number: ")

        if not account_number.isdigit():
            print("Account number must contain only digits")
            continue

        account_number = int(account_number)

        duplicate = False

        for account in accounts:
            if account["account_number"] == account_number:
                duplicate = True
                break

        if duplicate:
            print("Account number already exists")
        elif account_number <= 0:
            print("Account number must be greater than 0")
        else:
            break

    while True:
        initial_deposit = float(input("Enter Initial Deposit: "))

        if initial_deposit > 0:
            break
        else:
            print("Initial deposit cannot be negative or zero")

    account = {
        "account_number": account_number,
        "name": name,
        "balance": initial_deposit,
        "transactions": [],
    }

    if initial_deposit > 0:
        account["transactions"].append(f"Initial Deposit: {initial_deposit:.2f}")

    accounts.append(account)

    print("Account created successfully")


def find_account():
    account_number = int(input("Enter Account Number: "))

    for account in accounts:
        if account["account_number"] == account_number:
            return account

    return None


def deposit():
    if len(accounts) == 0:
        print("No accounts available.")
        return

    account = find_account()

    if account is None:
        print("Account not found.")
        return

    while True:
        amount = float(input("Enter Deposit Amount: "))

        if amount > 0:
            break
        else:
            print("Deposit amount must be greater than 0")

    account["balance"] += amount

    account["transactions"].append(f"Deposit: +₹{amount:.2f}")

    print(f"₹{amount:.2f} deposited successfully.")
    print(f"Current Balance: ₹{account['balance']:.2f}")


def withdraw():
    if len(accounts) == 0:
        print("No accounts available.")
        return

    account = find_account()

    if account is None:
        print("Account not found.")
        return

    while True:
        amount = float(input("Enter Withdrawal Amount: "))

        if amount <= 0:
            print("Withdrawal amount must be greater than 0")
        elif amount > account["balance"]:
            print("Insufficient balance.")
        else:
            break

    account["balance"] -= amount

    account["transactions"].append(f"Withdrawal: -₹{amount:.2f}")

    print(f"₹{amount:.2f} withdrawn successfully")
    print(f"Current Balance: ₹{account['balance']:.2f}")


def check_balance():
    if len(accounts) == 0:
        print("No accounts available")
        return

    account = find_account()

    if account is None:
        print("Account not found.")
        return

    print(f"\nAccount Holder : {account['name']}")
    print(f"Account Number : {account['account_number']}")
    print(f"Balance       : ₹{account['balance']:.2f}")


def transaction_history():
    if len(accounts) == 0:
        print("No accounts availabl")
        return

    account = find_account()

    if account is None:
        print("Account not found.")
        return

    print(f"\n--- Transaction History ---")
    print(f"Account Holder: {account['name']}")

    if len(account["transactions"]) == 0:
        print("No transactions found")
        return

    for transaction in account["transactions"]:
        print(transaction)


while True:

    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Exit")

    choice = input("Enter your choice: ")

    match choice:

        case "1":
            create_account()

        case "2":
            deposit()

        case "3":
            withdraw()

        case "4":
            check_balance()

        case "5":
            transaction_history()

        case "6":
            break

        case _:
            print("Invalid choice")
