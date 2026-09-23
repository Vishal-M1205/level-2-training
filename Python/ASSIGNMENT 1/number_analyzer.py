import math

number = int(input("Enter a number : "))

print(f"Number of digits {len(list(str(number)))}")

sum = 0
for i in str(number):
    sum += int(i)
print(f"Sum : {sum}")

product = 0
for i in str(number):
    product *= int(i)
print(f"Product : {product}")

print(f"Reverse : {str(number)[::-1]}")

print("Even") if number % 2 == 0 else print("Odd")

if number > 1:
    for i in range(2, int(math.sqrt(number**0.5)) + 1):
        if number % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")

print("Palindrome") if str(number)[::-1] == str(number) else print("Not a Palindrome")

armstrong_sum = 0
power = len(str(number))
for i in str(number):
    armstrong_sum += int(i) ** power

if armstrong_sum == number:
    print("Armstrong")
else:
    print("Not an Armstrong")
