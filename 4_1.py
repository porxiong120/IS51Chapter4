
# def get_number():
#     return 5

# def set_number(num):
#     number = num 
#     print("From set_number, num is: ", str(num))
#     return number

# num = get_number()
# set_number(6)

# print("End of program. Num is: ", str(num))

# def add_number(num1, num2):
#     print("num1: ", str(num1))
#     print("num2: ", str(num2))
#     val = num1 + num2 
#     print("from add_number, val is: ", str(val))
#     return val 

# output = add_number(2, 5) #7
# print("Output of {} and {} is {}.".format(str(2), str(5), output))

#defining a function
def get_firstname(full_name): # Por Xiong 
    space = full_name.index(" ") 
    # print space will result in 3 - the index of the space 
    first_name = full_name[:space]
    return first_name

my_name = get_firstname("Por Xiong")
# # string concatenation, adding strings 
print("Hello, my name is: " + my_name + ".")  

names = ["Lucas Phan", "Joe Biden", "Mike Tyson", "Tom Brady", "Kobe Bryant"]

for name in names:
    my_name = get_firstname(name)
    #print("Name: ", name)
    # print("Hello, my name is: " + my_name + ".") 
    if my_name == "Tom":
        print(my_name + " plays football!")
    elif my_name == "Kobe":
        print(my_name + " plays basketball!")
    elif my_name == "Mike":
        print(my_name + " is into boxing!")
    else:
        print(my_name + " is not into sports!")
