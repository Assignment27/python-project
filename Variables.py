# Variable is a container used to hold/represent data

name ="larry"
print(name)

# DATATYPES

# --Numbers

# Python supports two types of numbers : integers(whole numbers) and floating point numbers(decimals).
# ( it also supports complex number,which will be explained later as we go further).

#Integer

myint = 7

print(myint)
print(myint + 3)

# Float

myfloat = 7.0
print(myfloat)

# --type()

print(type(name))
print(type(myint))
print(type(myfloat))

# STRING
# letters or series of character are known as string

text ="My name is larry"
print(text)

print(type(text))

# NOTE: every string data type must be enclosed in either double or single quote ("" OR '')
# the difference between this two is that using double quotes makes it easy to include apostrophe's

name = "larry's Phone"
lname = 'Thomzy \'s Phone' # \' phyton sees that as this: '


print(name, lname)

# BODLEAN
# BODLEAN data type is True or False

isMARRIED = False
isAdult = True

print(isMARRIED)
print(isAdult)

print(type(isMARRIED))

# There are certain rules to follow when naming your variable

# 1 Variables name can contain letters, numbers and underscore
# 2 Variables names cannot contain space
# 3 Variables name cannot start with a number
# 4 case matters, for instance, temp and TEMP are different
# 5 using descriptive name as your variables makes your program more understandable
