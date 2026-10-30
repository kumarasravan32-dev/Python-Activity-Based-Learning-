# Patient Bill Calculation
age = int(input("Enter patient age: "))
consultation = float(input("Consultation charge: "))
test = float(input("Test charge: "))
treatment = float(input("Treatment charge: "))

if consultation < 0 or test < 0 or treatment < 0:
    print("Invalid charges")
else:
    total = consultation + test + treatment

    if age >= 60:
        discount = total * 0.10
    else:
        discount = 0

    final_bill = total - discount

    print("Total bill:", total)
    print("Discount:", discount)
    print("Final bill:", final_bill)

    payment = float(input("Enter payment: "))

    if payment < 0 or payment > final_bill:
        print("Invalid payment")
    elif payment == final_bill:
        print("Fully paid")
    elif payment > 0:
        print("Partially paid")
    else:
        print("Not paid")
  