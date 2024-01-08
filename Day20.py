import os
# Calculator
def addition(a, b):
    return a + b
def substraction(a, b):
    return a - b
def multiplication (a, b):
    return a * b
def division(a, b):
    return a / b
function_dict= {
    "+" : addition,
    "-" : substraction,
    "*" : multiplication,
    "/" : division

}

def continue_op():

    number_1 = int(input("enter first number: "))
    flag = True
    while flag == True:
        for key in function_dict:
             print(key)
    
        symbol = input("enter the operation which you want to perform: ")
        number_2 = int(input("Enter your next number: "))
        if symbol in function_dict:
            calculator_operation = function_dict[symbol]  
            output = calculator_operation(number_1, number_2)
            print(f"{number_1} {symbol} {number_2} = {output}")
            continue_operation = input(f"Do you want to continue with {output} then enter 'y':  want to exit then enter 'x':  want a new operation then enter 'n':").lower()
            if continue_operation == 'y':
                number_1= output
            elif continue_operation == 'n':
                os.system('clear')
                flag = False
                continue_op()
            else:
                flag = False
                print("Bye... Have a nice Day !")
        else:
            print("Invaid Operation please try valid operation symbol")

continue_op()                


                           

    
