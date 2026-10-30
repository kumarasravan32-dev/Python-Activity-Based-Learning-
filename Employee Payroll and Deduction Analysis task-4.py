# Salary Calculation Program:
basic = float(input("Enter basic salary: "))
hours = int(input("Enter overtime hours: "))

allowance = basic * 0.20
incentive = basic * 0.05
overtime = hours * 200

gross = basic + allowance + incentive + overtime

if gross <= 20000:
    deduction = gross * 0.05
elif gross <= 40000:
    deduction = 1000 + (gross - 20000) * 0.10
else:
    deduction = 3000 + (gross - 40000) * 0.15

net = gross - deduction

print("Gross salary:", gross)
print("Deduction:", deduction)
print("Net salary:", net)
  