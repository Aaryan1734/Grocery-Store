import random

print("\nThe Best Grocery Store\n")

file = open("reciept.txt", "wt")
file.write("Thank You for Visiting Best Grocery Store! \nCheckout \n")

balance = random.randrange(10, 151, 5)
tax = 0.20
item = ''
quantity = 1
total = 0

inventory = {
  'Apple': 0.29,
  'Banana': 0.49,
  'Biscuits': 0.49,
  'Bread': 2.99,
  'Cold Drink': 0.99,
  'Grapes': 1.99,
  'Ice Cream': 2.99,
  'Lemon': 0.16,
  'Milk': 2.99,
  'Mixed Vegetables': 1.99,
  'Onion': 0.74,
  'Plantain Chips': 1.99,
  'Potato': 0.49,
  'Tomato': 0.34,
  'Yogurt': 1.99
}

items = []

print("The prices below are for each individual item.\n")
for product in inventory:
  print(f"{product}: ${inventory[product]}")
print(f"\nYour balance is ${balance}.00\n")

while balance > 0:
  item = input("Enter an item you want to buy, or press 's' to save ").title()
  # print(item in inventory.keys())
  # print(item)

  if item == 'S':
    break
  elif item in inventory.keys():
    quantity = int(input("How many of this item do you want to buy? "))
    prices = inventory.values()
    price = round((inventory[item]*quantity), 2)
    taxed_price = price*tax
    price += taxed_price
     
    if balance > price:
      balance -= price
      total += price
      item = f"{quantity} {item}: ${price} (+ tax)"
      items.append(item)
    if balance <= 0:
      print("Balance: $0\n")
    if balance > 0:
      print(f"Balance: ${round(balance, 2)}\n")
    if balance < min(prices):
      print("You cannot buy anything, balance is too low!")
      break
    total = round(total, 2)

for i in items:
  i = str(i+"\n")
  file.write(i)
file.write(f"Total: ${total}")
file.close()
