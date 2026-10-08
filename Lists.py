# List is similar to variables only that they contain multiple
# values. OR contain as many variables as you wish

name = "Larry" # Variable
names = ["Tose", "Wande", "Femi"] # List

# We create a list using the [] "square brackets"

names = [] # empty list
print(names)
names.append("Larry")
names.append("Wande")
names.append("Femi")
names.append("Tose")
names.append("Feyi")
names.append("Emmanuel")
print(names)

# append() is used to add values into a list.


# Lists can contain various/different datatypes
mylist = [1,2.718,"abc",[5,6,7]]
print(mylist)

# Lists Functions
# sum() - Adds up all the values in a list and return the result
nums = [5,2,4,8]
print(sum(nums))

# lens() - Gets the total number of values in a list
print("The length of this list is:", len(nums))
print("There are", len(names), "of us in python class")

# min() - Gets the minimum value in our list
print("The minimum value in the list is:", min(nums))

# max() - Gets the maximum value in our list
print("The maximum value in the list is:", max(nums))

average = sum(nums)/len(nums)
print("The average of the list is:", average)


# sort - will arrange the datas in ascending order
names.sort()
print(names)

# count - count the number of occurrence of a particular value
x = nums.count(5)
print(x)
y = nums.count(2)
print(y)

# index -- position of each value in our list (starting from 0)
mylist = ["crazy", "weird", "sustain", "abolish"]
print(mylist[0])
print(mylist[3])
print(mylist[1])


# SLICING
fruits = ["mango", "apple", "banana", "pineapple", "cherry", "guava", "orange", "watermelon", "avocado", "cabbage","pawpaw", "golden melon"]
print(fruits[:])
print(fruits[:5])
print(fruits[5:])
print(fruits[4:8])
print(fruits[2:8:2])
print(fruits[-1])
print(fruits[-5])
print(fruits[::-1])

# Reverse
# how to use a reverse
fruits.reverse()
print(fruits)

# Remove--
# its to remove an item by referring to its value itself
fruits.remove("golden melon")
print(fruits)

# Pop function--
# it removes an item by referring to its index
fruits.pop(6)
print(fruits)

# Insert function--
fruits.insert(1, "pear")
print(fruits)

# How to change list by replacing
fruits[1] = "cherry"
print(fruits)

# How to delete second item in the list
del fruits[1]
print(fruits)

# How to copy a list
name = "Larry"
myname = name
print(myname)

myfruit = fruits
print(myfruit)
# another method
ourfruit = fruits[:]
print(ourfruit)

# how to delete first two items in the lists
del fruits[:2]
print(fruits)





#