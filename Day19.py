def formatName(*args):
    formated_names = [names.title() for names in args]
    full_name = " ".join(formated_names)
    return full_name


print(formatName("akshay","bombale","jay","virat","maruthi"))

# #Excersise
def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0: 
        return True
    else:
        False

def dayInMonth(year, month):
    days_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    if leap_year(year) and month == 2:
        return 29
    else:
        return (days_list [month-1])
     
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = dayInMonth(year, month)
print(day)

#Exercise
def fun_1(a, b):
    return a * b

def fun_2(x):
    return x * 2

output_1 = fun_1(3, 4)
print(fun_2(output_1))