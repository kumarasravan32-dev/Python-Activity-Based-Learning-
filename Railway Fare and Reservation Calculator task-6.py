# Train Ticket Fare Calculation Program:
n = int(input("Enter number of passengers: "))
distance = int(input("Enter distance in km: "))

if distance <= 100:
    rate = 1.5
elif distance <= 300:
    rate = 1.2
else:
    rate = 1

for i in range(n):
    age = int(input("Enter passenger age: "))
    travel_class = input("Enter class (sleeper/ac): ").lower()

    if travel_class == "ac":
        multiplier = 2
    else:
        multiplier = 1

    if age < 5:
        fare = 0
    else:
        fare = distance * rate * multiplier

        if age >= 60:
            fare = fare * 0.80

        fare = fare + 40

    print("Passenger fare:", fare)

    cancel = input("Cancel ticket? (yes/no): ")

    if cancel == "yes":
        print("Cancellation penalty:", fare * 0.25)
  