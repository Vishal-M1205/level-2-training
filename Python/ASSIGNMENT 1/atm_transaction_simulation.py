def setpin(validate=False):
    while True:
        pin = int(input("Enter ATM Pin : " if validate else "Set ATM Pin : "))
        if pin > 999 and pin <= 9999:
            break
        else:
            print("Invalid Pin, pin should be 4-Digit")
    return pin


def deposit():
    while True:
        amount = int(input("Enter Amount : "))
        if amount > 0:
            break
        else:
            print("Invalid Amount")
    return amount


def withdraw(balance):
    while True:
        amount = int(input("Enter Amount : "))
        if amount < 0:
            print("Invalid Amount")
        elif amount <= balance:
            balance -= amount
            break
        else:
            print("Insufficent Balance")
            break
    return balance


def validatePin(valid_pin):
    attempt = 3
    while attempt > 0:
        pin = setpin(True)
        if pin == valid_pin:
            return True
        else:
            attempt -= 1
            print(f"Invalid Pin : {attempt} left!")
    return False


openATM = True
pin = setpin()
balance = 0
while openATM:
    print(
        "Options :\n 1. Check Balance\n 2. Deposit\n 3. Withdraw\n 4. Change PIN\n 5.Exit"
    )
    option = int(input("Choose a Option : "))

    match option:
        case 1:
            if validatePin(pin):
                print(f"Balance : {balance}")
            else:
                openATM = False
        case 2:
            if validatePin(pin):
                balance += deposit()
                print("Amount Deposited")
            else:
                openATM = False
        case 3:
            if validatePin(pin):
                balance = withdraw(balance)
            else:
                openATM = False
        case 4:
            if validatePin(pin):
                pin = setpin()
            else:
                openATM = False
        case 5:
            openATM = False
        case _:
            print("Invalid Option")
