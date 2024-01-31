#tuples and operations
tuple_1 = (2,5,1,7,4,"Akshay",90)
tuple_2 = (7,3,90,21,4,90)
print(tuple_1,tuple_2)
print(len(tuple_1))
print(min(tuple_2))
print(max(tuple_2))
print((tuple_2 + tuple_1))

#sets and methods
set_1 = {4,76,34,43,101,102,103,104,100}
set_2 = {101,102,103,104,100} 
set_1.union(set_2)
print(set_1)
print (set_1 | set_2)
print(set_1.union((100,101,102)))
print(set_1.intersection(set_2))
print (set_1 & set_2)
set_2.intersection_update([32]) 
print(set_2)
print(set_1-set_2) #set_1.difference(set_2)
set_1.difference_update(set_2)
print(set_1)
print(set_1.symmetric_difference(set_2)) #in this it not return comman element
print(set_1 ^ set_2)
print(set_1.isdisjoint(set_2))
print(set_1.issubset(set_2))
print(set_1.issuperset(set_2))
