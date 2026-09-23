import math

while True:
    print(
        "1. Check Even/Odd\n"
        "2. Check Prime\n"
        "3. Check Palindrome\n"
        "4. Check Armstrong\n"
        "5. Reverse Number\n"
        "6. Sum of Digits\n"
        "7. Exit"
    )
    option = int(input("Enter a option : "))

    match option:
        case 1:
            number = int(input("Enter a Number : "))
            print("Even") if number % 2 == 0 else print("Odd")
        case 2:
            number = int(input("Enter a Number : "))
            if number > 1:
                for i in range(2, int(math.sqrt(number**0.5)) + 1):
                    if number % i == 0:
                        print("Not Prime")
                        break
                    else:
                        print("Prime")
            else:
                print("Not Prime")

        case 3:
            number = int(input("Enter a Number : "))
            (
                print("Palindrome")
                if str(number)[::-1] == str(number)
                else print("Not a Palindrome")
            )
        case 4:
            number = int(input("Enter a Number : "))
            armstrong_sum = 0
            power = len(str(number))
            for i in str(number):
                armstrong_sum += int(i) ** power

            if armstrong_sum == number:
                print("Armstrong")
            else:
                print("Not an Armstrong")
        case 5:
            number = int(input("Enter a Number : "))
            print(f"Reverse : {str(number)[::-1]}")
        case 6:
            number = int(input("Enter a Number : "))
            sum = 0
            for i in str(number):
                sum += int(i)
            print(f"Sum : {sum}")
        case _:
            break
