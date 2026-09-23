def discount(amnt):
    if amnt > 10000:
        return amnt * 0.4
    elif amnt > 5000:
        return amnt * 0.3
    else:
        return amnt * 0.2


no_products = int(input("Enter number of Products : "))

sub_total = 0
discounted_price = 0

for p in range(1, no_products + 1):
    while True:
        amnt = int(input(f"Enter Product {p} Price : "))
        if amnt > 0:
            sub_total += amnt
            break
        else:
            print("Invalid Amount")
    print(f"Subtotal : {sub_total}")
    discounted_price = sub_total - discount(sub_total)
    print(f"Discounted Price : {discounted_price}")

tax = discounted_price * 0.12

final_amount = discounted_price + tax

print(f"Tax : {tax}")
print(f"Final Amount : {final_amount}")
