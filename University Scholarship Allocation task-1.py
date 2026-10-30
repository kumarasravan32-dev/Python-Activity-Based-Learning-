#University_Scholarship_Allocation

n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter name: ")
    m1 = int(input("Enter subject 1 marks: "))
    m2 = int(input("Enter subject 2 marks: "))
    m3 = int(input("Enter subject 3 marks: "))
    attendance = int(input("Enter attendance: "))
    income = int(input("Enter family income: "))

    average = (m1 + m2 + m3) / 3

    if (average >= 80 and m1 >= 60 and m2 >= 60
        and m3 >= 60 and attendance >= 75
        and income <= 300000):
        print(name, "Is Eligible for scholarship")
    else:
        print(name, "Is Not eligible")
  