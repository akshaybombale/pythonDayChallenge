# #datatypes

var_1 = 23843654
var_2 = 345.43
var_3 = "Akshay"
var_4 = True

print(type(var_1))
print(type(var_2))
print(type(var_3))
print(type(var_4))

# #type casting

length = len("Akshay Bombale")
print("In your name there are " + str(length) + " charachter")

Number = input("enter any numbers: ")

firstNumber = Number[0]
secondNumber = Number[1]

print(int(firstNumber) + int(secondNumber))

# Arithmetic operator

a = 5
b = 2
print(a + b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)


x = 5
y = 6
print(x, y)
z = x + y
z += 2  
print(z)

# # Assignment Operator

print (z == 13)
print (z <= 13)
print (z >= 13)
print (z != 13)

# # Logical Operator if you want to check two conditions

p, q = 5, 8
print (p<q and q>5)
print (p<q or q>5)

m = 5
n = '5'
print (id(m)==id(n))

# # membership operator
# # in 
# # not in 

str =  "Akshay"
print ('y' in str)

list =  [65,8,45,43,43,23]
print(8 in list)
