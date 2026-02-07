print("------ Welcome to Billing Software ------")

bill = 0
items = int(input("How many items you want to buy? "))

for i in range(items):
    name = input(f"Enter name of item {i+1}: ")
    price = float(input(f"Enter price of {name}: "))
    qty = int(input(f"Enter quantity of {name}: "))
    
    total = price * qty
    bill += total
    print(f"{name} x {qty} = {total}")

print("---------------------------------")
print(f"Total Bill Amount: {bill}")
print("------ Thank You! Visit Again ------")
