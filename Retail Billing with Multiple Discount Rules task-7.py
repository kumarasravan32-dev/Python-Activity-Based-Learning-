#Billing System Program:
n = int(input("Enter number of products: "))
total = 0

for i in range(n):
    name = input("Enter product name (or 'done' to finish): ")
    if name.strip().lower() == "done":
        break
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    amount = price * quantity
    total = total + amount

if total > 5000:
    discount = total * 0.10

    if discount > 1000:
        discount = 1000
else:
    discount = 0

after_discount = total - discount
tax = after_discount * 0.12
final_bill = after_discount + tax

print("Total:", total)
print("Discount:", discount)
print("Tax:", tax)
print("Final bill:", final_bill)
  