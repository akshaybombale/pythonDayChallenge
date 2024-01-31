import random
import string
num = range(2,101,2)
sum=0
for i in num:
    sum += i
print(sum)  

# #Exercise
n = int(input("Enter the value of n: "))
print (n)
for i in range (1, n):
    if  i % 3 == 0 and   i % 5 == 0:
        print ("FizzBuzz") 
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif  i % 3 == 0 and   i % 5 == 0:
        print ("FizzBuzz") 
    else:
        print(i)

#Exercise
letters = list(string.ascii_letters)
symbols = list(string.punctuation)
numbers = list(string.digits)

letters_length = int(input("how many letters you want: "))
specialSymbols_length = int(input("how many special symbols you want: "))
numbers_length = int(input("how many Numbers: "))
password_string = []
for i in range(1,letters_length+1):
    char = random.choice(letters)
    password_string+=char
for j in range(1,specialSymbols_length+1):
    char_1 = random.choice(symbols)
    password_string+=char_1
for k in range(1,numbers_length+1):
    char_2 = random.choice(numbers)
    password_string+=char_2
random.shuffle(password_string)
password = " "
for i in password_string:
    password += i
print(password)     


