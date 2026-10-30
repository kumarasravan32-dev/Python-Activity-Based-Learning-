# Cost and Profit Calculation Program:
quantity = int(input("Enter quantity produced: "))
material = float(input("Material cost per unit: "))
labour = float(input("Labour cost per unit: "))
wastage = float(input("Wastage percentage: "))
machine = float(input("Machine cost: "))
selling = float(input("Selling price per unit: "))

material_cost = quantity * material
wastage_cost = material_cost * wastage / 100
labour_cost = quantity * labour

total_cost = material_cost + wastage_cost
total_cost = total_cost + labour_cost + machine

revenue = quantity * selling
profit = revenue - total_cost
target = total_cost * 0.20

print("Total cost:", total_cost)
print("Revenue:", revenue)
print("Profit:", profit)

if profit >= target:
    print("Profit target achieved")
else:
    print("Profit target not achieved")
  