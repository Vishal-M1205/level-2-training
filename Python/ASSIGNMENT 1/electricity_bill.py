customer_name = input("Enter your Name : ")
while True:
    units_consumed = int(input("Enter Consumed Units : "))
    if units_consumed >= 0:
        break
    else:
        print("Invalid Units")

charges = 0

if units_consumed <= 100:
    pass
elif units_consumed > 100 and units_consumed <= 300:
    charges = (units_consumed - 100) * 2
elif units_consumed > 300:
    charges = 200 * 2 + (units_consumed - 300) * 4

tax = units_consumed * 0.5

total_bill = tax + charges

print(f"Name : {customer_name}")
print(f"Units : {units_consumed}")
print(f"Charges : {charges}")
print(f"Tax : {tax}")
print(f"Total Bill : {total_bill}")
