# Python Functions
# A functions is a block of code that performs a specific task and can be reused whenever needed.
# A function is a block of code which only runs when it is called.
from email import message


# A function can return data as a result.

# A functions helps avoiding code repetition.

# WORA -- Write Once Run Anytime/Anywhere


# Functions are defined using the block keyword "def", followed with the function's
# name as the block's name.

def my_function():
    print("Hello from my Function")
my_function()


# To call a function, write its name followed by parenthesis:

# Function names

# Function names follow the same rules as variable names in python:

# A function name must start with a letter or underscore
# A Function name can only contain letters, numbers and underscores
# Function names are case-sensitive (myFunction and myfunction are different)
# it's good practice to use descriptive names that explain what the function does
# For examples:

def my_function_with_args(username, greeting):
    print("Hello, %s, From my Function! I wish you %s"%(username,greeting))

my_function_with_args("Larry", "Happy Married LIfe")
my_function_with_args("Daniella", "Happy Birthday")
my_function_with_args("Maro", "Happy easter")

# Function may return a value to the caller, using keyword- 'return'.
# For example

def sum_two_numbers(a, b):
    return a + b

ans = sum_two_numbers(2, 3)
print(ans)

print(sum_two_numbers(4, 5))

# Why use functions?
# Imagine you need to convert temperatures from Fahrenheit to Celsius several times in your program.
# Without functions, you would have to write the same calculation code repeatedly

temp1 = 77
celSius1 = (temp1 - 32) * 5 / 9
print(celSius1)

temp2 = 95
celSius2 = (temp2 - 32) * 5 / 9
print(celSius2)

temp3 = 50
celSius3 = (temp3 - 32) * 5 / 9
print(celSius3)

# WORA: Write Once Run Anytime/Anywhere.
# With functions, you write the code once and reuse it:

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))


# Return Values
# Functions can send data back to the code that called
# them using the return statement
# When a functions reach a return statement, it stops executing and send the result back.

def get_greeting():
    return "Hello from a function"

message = get_greeting()
print(message)


# You can use the returned value directly:

def get_greeting():
    return "Hello from a function"

print(get_greeting())


# If a function doesn't have a return statement, it returns none by default.

def say_name(name):
    return name

myname = say_name("Emmanuel")
print(myname)
print(myname)


# The Pass Statement
# Function definitions cannot be empty.
# If you need to create a function placeholder without any code, use pass statement

def my_function():
    pass

# The pass statement is often used when developing, allowing you to define the structure first and implement details.

# Temperature
# Problem:
# Write a function convert_temp() that takes a temperature and a scale ("C" for Celsius, "F" for Fahrenheit)

def convert_temp(temp, scale):
    if scale == "C":
        return (temp * 9/5) + 32
    elif scale == "F":
        return (temp - 32) * 5/9
    else:
        return "Invalid Scale"
print(convert_temp (100, "F"))
print(convert_temp(212, "C"))

# ATM Withdrawal stimulator
# Problem:
# Create a function withdraw(balance, amount)
# that checks if the amount is less than or equal to the balance
# If yes, subtract it and return the new balance:
# otherwise return "Insufficient Funds"

def withdraw(balance, amount):
    if amount <= balance:
        balance -= amount
        return f"Withdrawal Successful {amount}"
    elif amount <= balance:
        amount += balance
        return f"Insufficient Funds {balance}"
print(withdraw(5000, 2000))