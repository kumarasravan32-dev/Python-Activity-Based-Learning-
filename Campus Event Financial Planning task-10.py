# Event Cost and Income Calculation Program:
venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
transport = float(input("Enter transport cost: "))
food = float(input("Enter food cost per person: "))
certificate = float(input("Enter certificate cost per person: "))
fee = float(input("Enter registration fee per person: "))
sponsor = float(input("Enter sponsorship amount: "))

fixed = venue + equipment + transport
variable = food + certificate

if fee <= variable and sponsor < fixed:
    print("Break-even is not possible with this fee")
else:
    if sponsor >= fixed:
        minimum = 0
    else:
        minimum = (fixed - sponsor) / (fee - variable)
        minimum = int(minimum)

        if minimum < (fixed - sponsor) / (fee - variable):
            minimum = minimum + 1

    print("Minimum registrations:", minimum)

    participants = int(input("Enter expected participants: "))

    cost = fixed + participants * variable
    income = sponsor + participants * fee
    difference = income - cost

    print("Total cost:", cost)
    print("Total income:", income)

    if difference >= 0:
        print("Surplus:", difference)
    else:
        print("Shortfall:", -difference)
  