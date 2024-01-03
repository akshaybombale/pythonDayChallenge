# Exercise
weight = input("Enter your weight ")
Height = input("Enter your Height in mtr ")

BMI = int(weight) / float(Height) ** 2

print(int(BMI))

# f string use
Name = "Akshay"
Age = 26
Address = "pune"

print(f"My Name is {Name} and age is {Age} and Im living in {Address}")

#Exercise
currentAge = int(input("Enter your currentAge: "))
yearsLeft = 90 - currentAge
totaldays = yearsLeft * 365
totalMonths = yearsLeft * 12
totalWeeks = yearsLeft * 52

print(f"you have total {yearsLeft} years, {totalMonths} months, {totalWeeks} weeks and {totaldays} days left")
  