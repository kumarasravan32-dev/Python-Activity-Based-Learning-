# Electricity Bill Calculation:
n = int(input("Enter number of months: "))
previous = 0

for i in range(n):
    units = int(input("Enter units consumed: "))

    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = 200 + (units - 100) * 3
    else:
        bill = 500 + (units - 200) * 5

    bill = bill + 50
    print("Electricity bill:", bill)

    if previous > 0 and bill > previous * 1.3:
        print("Unusual increase in bill")

    previous = bill
  