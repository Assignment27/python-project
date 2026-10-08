# Python conditions and if statements
# Python supports th usual logical conditions from mathematics

# Equals a == b
# Not Equals : a ! = b
# Less than a > b
# Greater than a > b
# Greater than or equal to: a >= b
# Less than or equal to: a <= b

# These conditions can be used in several ways,
# most commonly in "if statements" and loops

# An "if statement" is written by using the if keyword.

a = 30
b = 300

if b > a:
    print("b is greater than a")

# checking if a number is positive:
number = 15
if number > 0:
    print("The number is positive")

# Indentation
# python relies on indentation (whitespace at the beginning of a line)
# to define scope in the code

# Other programming languages often use curly-braces for this purpose
# If statements without indentation (will raise an error):
a = 33
b = 200

if b > a:
    print("b is greater than a")

# Note: You can use spaces or tabs for indentation,
# but you must use the same amount of indentation for all
# statements within the same code block.
age = 21
if age >= 18:
    print("You are an adult")
    print("You can vote")
    print("You have full legal rights")

# Boolean variables can be used directly in if statement without
# comparison operators
# Using a boolean variable:

is_looged_in = True
if is_looged_in:
    print("welcome back")

# Python can evaluate many types of values as True or False
# in an if statements.

# Zero (0), empty string (""), None, and empty collections
# are treated as False, Everything else are treated as True.

# This includes positive numbers (5), negative numbers (-3),
# and any non-empty string, (even "False" is treated as True
# because it's a non-empty string)

x = 0
if x:
    print("This is True")

# The Elif Keyword
# The elif Keyword is Python's way of saying
# "if the previous conditions were not true, then try this condition

# The elif keyword allows you to check multiple expressions for True
# and execute a block of code as soon as one of the conditions evaluates to True

a = 33
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# Multiple Elif Statement
# You can have as many elifs statements as you need.
# Python will check each condition in order and execute the first
# one that is true.

score = 75
if score >= 90:
    print("Grade : A")
elif score >= 80:
    print("Grade : B")
elif score >= 70:
    print("Grade : C")
elif score >= 60:
    print("Grade : D")

# Important: only the first true condition will be executed.
# Even if multiple conditions are true,
# Python stops after executing the first matching block.

age = 21
if age < 13
    print("You are a child")
elif age < 20:
    print("You are a teenager")
elif age < 65:
    print("You are an adult")
elif age >= 65:
    print("You are a senior man")

# When to use ElIF
# Use elifs when you have multiple mutually exclusive conditions to check.
# This is more efficient than using multiple separate if statements
# because Python stops checking once it finds a true condition.

# Day of he wek checker
day = 3
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")

# The Else keyword
# The else keyword catches anything which isn't
# caught by the preceding conditions.

# The else statement is executed when the if condition
# (and any elif conditions) evaluate to False.

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# Else without Elif
# You can also have an else without the elif:

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# This creates a simple two-way choice: if the condition is true,
# execute one block; otherwise, execute the else block'

# Note: The else statement must come last.
# You cannot have an elif after an else.

# Even or Odd Checker
number = 8
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

