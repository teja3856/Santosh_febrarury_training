name = input("Enter Customer Name: ")
price = float(input("Enter Product Price: "))
premium_input = input("Is the customer a premium member? (True/False): ")
coupon = input("Enter Coupon Code: ")

is_premium = True if premium_input == "True" else False

discount = 0

if price > 5000 and is_premium:
    discount = 0.20 * price
elif is_premium or coupon == "SAVE10":
    discount = 0.10 * price

final_price = price - discount

print("\n----- Billing Details -----")
print(f"Customer Name: {name}")
print(f"Original Price: {price}")
print(f"Discount Applied: {discount}")
print(f"Final Price: {final_price}")

if is_premium:
    print("Premium benefits applied")
