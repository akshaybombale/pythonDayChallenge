
# #control statements
Age = int(input("Enter your Age: "))

if Age >= 25:
    print("Adult")
    print("you can be take responsibility for your family")
else:
    print("you are teen Ager")


Number = int(input("Enter any number: "))
if Number % 2 == 0:
    print("Number is Even Number")
else:
    print("number is Odd number")         


# #nested if, elif and else
    
Height = int(input("Enter the height of the rider: "))
bikerAge = int(input("Enter the Biker Age: "))
if (Height >= 5):
    print ("you can ride Bike")
    if (bikerAge < 18):
        print("pls pay 500 Rs")
    elif(bikerAge == 18):
        print("pls pay 250 rs")
else: 
    print("you can't ride Bike")
print("Bye !!!")   

#Excercise

weight = input("Enter your weight ")
Height = input("Enter your Height in mtr ")
BMI = int(weight) / float(Height) ** 2
print(int(BMI))
      
