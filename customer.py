products = ["Shoes:", "Clothes:", "Smartphone:", "Smart Watch:", "Bluetooth Speaker:"]
prices = {}
total = 0

for item in products:
    price = float(input(f"Enter price of {item}: "))
    prices[item] = price
    total += price

print("\n--- Bill ---")
for item, price in prices.items():
    print(f"{item}: Rs. {price}")
print("Total Purchase Amount: Rs.", total)
