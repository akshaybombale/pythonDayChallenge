
#Exercise 1  
year = int(input("enter the year: "))

if year % 4 == 0:
    
    if year % 100 == 0:

        if year % 400 == 0:
            print("leap year")

        else:
            print("this is not a leap year")     

    else:
        print("leap year")     

else:
    print("this is not a leap year")     


#exercise 2
Height = int(input("Enter the height of the rider: "))
bikerAge = int(input("Enter the Biker Age: "))
bill = 0
if (Height >= 5):

    print ("you can ride Bike")
    if (bikerAge < 12):
        bill = 150
        print(f"Ticket price is {bill} Rs")

    elif(bikerAge <= 18):
        bill = 250
        print(f"Ticket price is {bill} Rs")

    elif (bikerAge > 18):
        bill = 300
        print(f"Ticket price is {bill} Rs")  

    wantPhoto = (str(input("Do you want photo (Y/N): "))) 
    if wantPhoto == 'N':
        print(f"Your total bill is {bill} Rs")
    elif wantPhoto == 'Y':
        bill = bill + 50 
        print(f"Your total bill is {bill} Rs")

else: 
    print("you can't ride Bike")
print("Thanks for visit...Bye !!!") 

#Exercise 3

print("*******************Pizza order program************************")
pizzaSize = int(input("Choose pizza size \n1.Small Pizza \n2.Medium pizza \n3.Large pizza \n"))
print(f"you have choose {pizzaSize}")
amount=0
if pizzaSize == 1:
    amount += 100
    
elif pizzaSize == 2:
    amount += 200
   
elif pizzaSize == 3:
    amount += 300

pepporni = str(input("Do you want pepporni (Y/N):"))
if  pepporni == 'Y' and pizzaSize == 1:
    amount += 30

elif  pepporni == 'Y' and (pizzaSize == 2 or pizzaSize == 3):
    amount += 50

elif pepporni == 'N' and (pizzaSize == (1 or 2 or 3)):
    amount = amount 

  
Extrachees = str(input("Do you want extra chees (Y/N): "))
if Extrachees == 'Y':
    amount += 30
    print (f"your total bill is {amount} RS")
else:    
    print (f"your total bill is {amount} RS")
  






      