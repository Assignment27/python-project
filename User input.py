import math

# User input
# Python allows for user input
# That means we are able to ask for the user for input.

# The following examples asks for your name, and when you
# enter a name, it gets printed on the screen:

print("Enter your name:")
name = input()
print("Hello",name)

# Python stops executing when it comes to the input() function'
# and continues when the user has given some input

# Using prompt
# In the example above, the user had to input
# their name on a new line

# The python input() function has a prompt parameter, which
# acts as a message

# you can put it in front of the user input, on the same line:

name = input("Enter your name:")
print("Welcome",name)

# Multiple Inputs
# you can add as many inputs as you ant,
# python will stop executing at each of them,waiting for user input:

name = input("Enter your name:")
print("Hello",name)
fav1 = input("What is your favorite animal:")
fav2 = input("What is your favorite color:")
fav3 = input("What is your favorite number:")

print("Do you want a ",fav2,fav1, "with", fav3,"legs?")

# Input Number
# The input from the user is treated as a string. Even if you input a number,
# the python interpreter will still treat it as string.

# You can convert the input into a number with the float(), int() function:
# To find the square root, the input has to be converted into a number:

x = input ("Enter a number:")
# square root of x:
y = math.sqrt(int(x))
print("The square root of ",x,"is",y)

# TypeCasting
num1 = int(input("Enter a number:"))
num2 = int(input("Enter a second number:"))
print(num1 + num2)

name = input("Enter your name:")
age = input("What is your age")
clas = input("What is your class")

print("hey" , name , "you are" , age, "years old  and you are in  class" , clas )

