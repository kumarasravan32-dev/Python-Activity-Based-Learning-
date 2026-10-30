# Internet Data Plan Selection Program:
data = int(input("Enter required data in GB: "))
days = int(input("Enter required validity: "))
budget = int(input("Enter your budget: "))

if data <= 2 and days <= 28 and budget >= 199:
    print("Choose Basic Plan - Rs.199")

elif data <= 5 and days <= 56 and budget >= 299:
    print("Choose Standard Plan - Rs.299")

elif data <= 10 and days <= 84 and budget >= 399:
    print("Choose Premium Plan - Rs.399")

else:
    print("No suitable plan available")
  