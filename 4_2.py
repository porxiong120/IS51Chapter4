# def main():
#     first()
#     print(str(4) + ": from function main")

# def first():
#     print(str(1) + ": from function first")
#     second()
#     print(str(3) + ": from function first")

# def second():
#     print(str(2) + ": from function second")

# main()


# list1 = ["a", "e", "i", "o", "u"]

# for x in list1:
#     print("x: ", x)
#     # print("x: ", x.upper()) - capitalize the letters

# def f(y): 
#     return y.upper()


# list1 = ["a", "e", "i", "o", "u"]
# list2 = []

# def f(y): 
#     return y.upper()

# for x in list1:
#     print("x: ", x)
#     list2.append(f(x))

# print("List2: ", list2)

# list1 = ["a", "e", "i", "o", "u"]
# #list2 = []

# def f(y): 
#     return y.upper()

# #for x in list1:
# #    print("x: ", x)
# #    list2.append(f(x))

# #print("List2: ", list2)

# list2 = [f(x) for x in list1]
# list2 = [x.upper() for x in ["a", "e", "i", "o", "u"]]
# print("List2: ", list2)

# print("List: ", [x.upper()
#     for x in ["a", "e", "i", "o", "u"] if x in ["i", "o"]])

def total(arg1, arg2, arg3=10, arg4=20):
    arg1 = arg1 + 10
    arg2 = arg2 + 10
    print("From within total() arg1: ", arg1)
    print("From within total() arg2: ", arg2)
    return (arg1 ** arg2) + arg3 + arg4

# pass by value (parameters)
#total(2, 3) # work
#total(2, 3, 4) # work 
#total(2, 3, 3, 4) # work 
# total(2, 3, 3, 4, 5) # dont work - only 4 parameters 

arg1 = 2 
arg2 = 3 

print("From outside total() arg1: ", arg1)
print("From outside total() arg2: ", arg2)
#immutable, passing by reference (variables)
#total(arg1, arg2) 
total(arg2=5, arg1=2) 



