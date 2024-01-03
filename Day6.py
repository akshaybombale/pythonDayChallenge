import random

# use of list


List = [ 12,88,434,23,765,434,12, 12, 323,5]
print(List.count(12))
print(List.index(434))
print(List[2:5])
print(List.pop())
print(List.append(34))
print(List.sort())
print(List.reverse())
print(List)

#random module

l= random.choice(List)
print(random.randint(1,8)) 
print(random.randrange(4,9))
print(l)

#Exercise

side = random.randint(0,1)
if side == 0:
    print("Heads")
else:
    print("tails")



#Exercise
Names = input("enter the name of your group members: ")
nameList = Names.split(",")
print(nameList)
payer = random.choice(nameList)
print(f"{payer} will pay the bill this time")

#or

total_member = len(nameList)
bill_payer = random.randint(0, total_member -1 )
print(f"{bill_payer} will pay the bill this time")

#nested list 
nested_List = [45,7,34,23,[57,34,23,56],45]
print (len(nested_List))
print(nested_List[4][0:3]) # for to print the nested list's one and one element

