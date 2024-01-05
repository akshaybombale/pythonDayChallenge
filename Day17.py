#dictionary

employee = {
    'Name': "Akshay",
    'Mob':8668469066,
    'Add':"pune"
    }
print(employee)
print(employee['Mob'])
employee['Mob']={9970929035,8567546756}
print(employee)
employee['Name']={'real_name':"hello",'nick_name':'Hi'}
print(employee['Name']['real_name'])

Data = {
    1:'Akshay',
    2:'Vishal',
    0:'sanket'
}

print(Data[0])
del Data[0]
print(Data)
print(Data.values())
print(Data.pop(2))
print(employee.items())
for key in employee:
    print(employee[key])

#Excercise
students_data = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78,
    'David': 95,
    'Eva': 88,
    'Frank': 76,
    'Grace': 90,
    'Harry': 87,
    'Ivy': 94,
    'Jack': 82
}  

students_Grade = {

}

for name in students_data:
    marks = students_data[name]
    if marks>=90:
        students_Grade[name]="A+"
    elif marks>=80:
        students_Grade[name]="A"
    elif marks>=70:
        students_Grade[name]="B+"
    elif marks>=60:
        students_Grade[name]="B"
    elif marks>=50:
        students_Grade[name]="C+"
    elif marks>=40:
        students_Grade[name]="C"
    else:
        students_Grade[name]="Fail"    

print(students_Grade)   

#nested dict
students = {
    'Alice': {
        'Math': 85,
        'English': 90,
        'Science': 88
    },
    'Bob': {
        'Math': 92,
        'English': 85,
        'Science': 89
    },
    'Charlie': {
        'Math': 78,
        'English': 80,
        'Science': 75
    },
    'David': {
        'Math': 95,
        'English': 92,
        'Science': 96
    },
    'Eva': {
        'Math': 88,
        'English': 86,
        'Science': 90
    }
 
}


# print(students['Bob']['Math'])
# print()
# print(students['Eva'].pop("Math"))
for student, subjects in students.items():
    print(f"{student}:")
    for subject, marks in subjects.items():
        print(f"{subject}:{marks}")
    print()



