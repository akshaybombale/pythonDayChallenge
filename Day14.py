# #function
# def sum(a, b):
#     c = a + b
#     print("sum is:", c)

# sum(1, 2)
# sum(78, 25)

# def names(n,s,d):
#     print(f"my name is {n}")
#     print(f"I'm learning {s}")
#     print(f"I'm from {d} department")

# names("Jay","python", d ="CS")    

# def names(n,s,d="Mech"):
#     print(f"my name is {n}")
#     print(f"I'm learning {s}")
#     print(f"I'm from {d} department")

# names("Jay","python")    

# def addition(*num):
#     sum = 0
#     for i in num:
#         sum+=i
#     print(sum)

# addition(1,2,3,4,5)

# # types of argumrnts
# # 1.Default
# # 2.posional
# # 3.keyword
# # 4.Arbitory

#     # - Arbitory positional argument
# def addition(*num):
#     sum = 0
#     for i in num:
#         sum+=i
#     print(sum)

# addition(1,2,3,4,5)


#     # - Arbitory key word Argument

# def info(**kwarg):
#     for key,value in kwarg.items():
#         print(key,value)

# info(name ="Akshay", age = 20, Address = "Pune", Mob = 8668469066 )        

#if both Arguments and key word arguments
def info(*args, **kwarg):
    for key,value in kwarg.items():
        print(key,value)
    print(args)    

info(1,2,3,name ="Akshay", age = 20, Address = "Pune", Mob = 8668469066 )      