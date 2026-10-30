# Foreign Currency Expense Tracker Program:

budget = float(input("Enter budget in rupees: "))
total = 0

for i in range(4):
    amount = float(input("Enter expense in foreign currency: "))
    rate = float(input("Enter exchange rate: "))

    rupees = amount * rate
    fee = rupees * 0.02
    expense = rupees + fee

    total = total + expense
    print("Expense in rupees:", expense)

print("Total spending:", total)
print("Remaining budget:", budget - total)

if total > budget:
    print("Budget exceeded")
else:
    print("Within budget")
  