# (FUNCTIONS)
#
# def say_hi(name, age):
#     print("Hello " + name + ", you are " + age)
#
# say_hi("Shreyansh", "14")
# say_hi("Kashyap", "20")
#
#
# (RETURN STATEMENT)
#
# def cube(num):
#   return  num*num*num
# print("code")
#
# result = cube(4)
# print(result)
#
#
# # (IF STATEMENTS)
#
## def max_num(num1, num2, num3):
#     if num1 <= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
#
#
# print(max_num(300,40 , 5))
# is_male = True
# is_tall = True
#
#
# if is_male or is_tall:
#     print("You are a tall male")
# elif is_male and not(is_tall):
#     print("You are a short male")
# elif not(is_male) and is_tall:
#     print("You are not a male but are tall")
# else:
#     print("You are not a man and not tall")


# (IF STATEMENTS AND COMPARISIONS)






# (BUILDING A BETTER CALCULATOR)

# num1 = float(input("Enter first number: "))
# op = (input("Enter operator: "))
# num2 = float(input("Enter second number: "))
#
# if op == '+':
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "/":
#     print(num1 / num2)
# elif op == "*":
#     print(num1 * num2)
# else:
#     print("Invalid operator")


# (DICTIONARIES)
#
# monthConversions = {
#     1: "January",
#     2: "February",
#     3: "March",
#     4: "April",
#     5: "May",
#     6: "June",
#     7: "July",
#     8: "August",
#     9: "September",
#     10: "October",
#     11: "November"
#     12: "December",
# }
#
# print(monthConversions.get(3))

#
# # (WHILE LOOP)
# #
# i = 1
# while i <= 11:
#      print(i)
#      i += 1
#
# print("Done with loop")


# (BUILDING A GUESSING GAME)

# secret_word = "lion"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
#
# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input("Enter guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
#
# if out_of_guesses:
#     print("Out of Guesses, YOU LOSE!")
# else:
#     print("You win!")



#(FOR LOOP)


# friends = ["Yash", "Hirensh", "Viswaraj"]
# for index in range(5):
#      if index == 0:
#           print("first Interation")
     # else:
          # print("Not First")




# (EXPONENY FUNCTION)

# def raise_to_power(base_num, pow_num):
#      result = 1
#      for index in range(pow_num):
#           result = result * base_num
#      return result
#
# print(raise_to_power(3, 2))


#(2D LISTS AND NESTED LOOPS)


# number_grid = [
#      [1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9],
#      [0]
# ]
# 
# for row in number_grid:
#      for col in row:
#           print(col)



# Build a Translator...


# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#          if letter in "AEIOUaeiou":
#              translation = translation + "g"
#          else:
#              translation = translation + letter
#     return translation

# print(translate(input("Enter a phrase: ")))



#Comments....

# comments are fun


#Try / Except...

# try:
#   number = int(input("Enter a number: "))
#   print(number)
# except ZeroDivisionError:
#   print("Divided by zero")
# except ValueError:
#   print("Invalid input")



#Reading Files....


# employee_file = open("employees.txt", "r")
# for employee in employee_file.readlines():
#   print(employee)
# employee_file.close()


#Writting Files...


# employee_file = open("index.html", "w")

# employee_file.write("<p>This is html</p>")

# employee_file.close()




#Modules and pip...

# import useful_tools

# print(useful_tools.roll_dice(10))


# import docx


#Classes and Objects....


