
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
# def get_firstname(full_name): # Por Xiong 
#     space = full_name.index(" ") 
#     # print space will result in 3 - the index of the space 
#     first_name = full_name[:space]
#     return first_name

# my_name = get_firstname("Por Xiong")
# # # string concatenation, adding strings 
# print("Hello, my name is: " + my_name + ".")  

# names = ["Lucas Phan", "Joe Biden", "Mike Tyson", "Tom Brady", "Kobe Bryant"]

# for name in names:
#     my_name = get_firstname(name)
#     #print("Name: ", name)
#     # print("Hello, my name is: " + my_name + ".") 
#     if my_name == "Tom":
#         print(my_name + " plays football!")
#     elif my_name == "Kobe":
#         print(my_name + " plays basketball!")
#     elif my_name == "Mike":
#         print(my_name + " is into boxing!")
#     else:
#         print(my_name + " is not into sports!")

# 4/26/22

# def pay(wage, hours):
#     amount = 0
#     if hours <= 40:
#         print("Here!")
#         amount = wage * hours 
#     else:
#         amount = (wage * 40) + ((1.5) * wage * (hours - 40))
#     return amount 

# hourlyWage = 50 
# hoursWorked = 40 

# result = pay(hourlyWage, hoursWorked)
# #print("result: ", result)
# print("Earnings: ${0:,.2f}".format(result))


# def pay(wage, hours):
#     amount = 0
#     if hours <= 40:
#         print("Here!")
#         amount = wage * hours 
#     else:
#         amount = (wage * 40) + ((1.5) * wage * (hours - 40))
#     return amount 

# hourlyWage = eval(input("Enter the hourly wage: "))
# hoursWorked = eval(input("Enter the numbers of hours worked: ")) 

# result = pay(hourlyWage, hoursWorked)
# #print("result: ", result)
# print("Earnings: ${0:,.2f}".format(result))


# def pay(wage, hours):
#     amount = 0
#     if hours <= 40:
#         print("Here!")
#         amount = wage * hours 
#     else:
#         amount = (wage * 40) + ((1.5) * wage * (hours - 40))
#     return amount 

# wage = eval(input("Enter the hourly wage: "))
# hours = eval(input("Enter the numbers of hours worked: ")) 

# result = pay(wage, hours)
# #print("Paycheck amount: ", result)
# print("Earnings: ${0:,.2f}".format(result))


# def is_vowel_word(word):
#     word = word.upper()
#     vowels = ('A', 'E', 'I', 'O', 'U')
#     for vowel in vowels:
#         if vowel not in word:
#             return False 
#     return True 

# word = input("Enter a word: ")
# if is_vowel_word(word):
#     print(word, "contains every vowel.")
# else:
#     print(word, "does not contain every vowel.")


# def is_vowel_word(word):
#     word = word.upper()
#     vowels = ('A', 'E', 'I', 'O', 'U')
#     for vowel in vowels:
#     #     if vowel not in word:
#     #         return False 
#     # return True 
#         return False if vowel not in word else True 
#         vowel in word 



# word = input("Enter a word: ")
# if is_vowel_word(word):
#     print(word, "contains every vowel.")
# else:
#     print(word, "does not contain every vowel.")


# PI = 3.141529
# def main():

#     # x = 2 
#     y = 2
#     # print(str(x) + ": function main")
#     print(str(y) + ": function main")
#     trivial()
#     # print(str(x) + ": function main")
#     print(str(y) + ": function main")


# def trivial():
#     x = 3
#     print (str(x) + ": function trivial")
#     #print y # can't b/c y trivial has no y 
#     print(PI)

# main()