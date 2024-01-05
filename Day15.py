import math

def numberOfCan(height,width,coverage):
    No_Of_can = 0
    No_Of_can = height * width / coverage
    print (math.ceil(No_Of_can))



height = int(input("enter height of the wall: "))
width = int(input("enter width of the wall: "))
numberOfCan(height,width,coverage = 7)   


#*****************************************************************************************


def prime(number):
    is_prime = True
    if number == 1:
       is_prime = False
    for i in range(2, math.ceil(number/2)+1):
        if number % i == 0:
            is_prime = False
    if is_prime == True:
        print("number is prime")
    else:
        print("number is not prime")

number = int(input("enter the number: "))
prime(number)

