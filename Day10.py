numbers = [3,7,9,4,1,8,-4]
squares = []
for i in numbers:
    square = i ** 2
    squares.append(square)
print(f"squares of the numbers is : {squares}")   

list = [ "Akshay", "Roshan", "Jay", "vaibhav"]
for names in list:
    print(names)
    if names == "Jay":
        break
else:
    print("Successfully completed")   


# #Exercise
num = input("enter the numbers for list:")
list = num.split()
count = 0
for i in list:
    count +=1
print(count)
for i in range(0, count):
    list[i] = int(list[i])
print(list)
total = 0
for i in list:
    total += i
print(total)
avg = total/count
print(round(avg))

# # OR

num = input("enter the numbers for list:")
list = num.split()
count = 0
for i in list:
    count+=1
for i in range(count):
    list[i]=int(list[i])
sum=sum(list)
print(round(sum/count))


#exercise 
list_1 = input("enter the numbers for list:")
list_num = list_1.split()
# count = 0
# for i in list_num:
#     count+=1
for i in range(0, len(list_num)):
    list_num[i]=int(list_num[i])
max_num = list_num[0]
for i in list_num:
    if i >  max_num:
        max_num = i 
print(max_num)   


            