# Dictionaries
# Dictionaries are used to store data values in key:value pairs

thisdict = {
    "brand" : "Ford",
    "Model" : "Mustang",
    "year" : 2000
}

print(len(thisdict))

# Dictionary DataTypes
# The values in dictionary items can be of any datatypes:

vehicle = {
    "brand": "Toyota",
    "electric": False,
    "year": 1965,
    "colors": ["silver", "black", "wine"]
}

# using the dict() constructor method to make a dictionary:

thisdict = dict(name = "Haaland", age =24, country = "Norway")
print(thisdict)

# Accessing items
# You can access the items of a dictionary by referring to its key name,
# inside square brackets [key]:

car = {
    "brand": "lamborghini",
    "model": "Revuelto",
    "year" : 2025
}

x = car["model"]
print(x)

y = car["year"]
print(y)

z = car["brand"]
print(z)

# There is also a method called get() that wil give you the
# same result:

y = car.get("model")
print(y)

# Getting the keys
# The keys() method will return a list of all the keys in the
# dictionary

x = car.keys()
print(x)

# Add a new item to the original dictionary,
# and see that the key list get updated as well

phone = {
    "brand": "Apple",
    "model": "iphone 15 pro max",
    "year": 2024

}

print(phone.keys()) # before the change

phone["color"] = "silver titanium" # new item

print(phone.keys()) # after change

# Get Values
# The values() method will return a list of all the values in
# the dictionary.

print(phone)

x = phone.values()
y = phone.keys()

print(x)
print(y)


# Change Values
# You can also change value of a specific item by referring to its key name:

house = {
    "type": "Bungalow",
    "color": "Brown",
    "rooms": 3
}

print(house) # before changing

house["color"] = "white"

print(house) # after changing

print(house)
house["rooms"] = 5
print(house)

# Update Dictionary
# The update() method will update the dictionary with the items
# from the given argument.

# The argument must be a dictionary, or an iterable object with
# key:value pairs.
# Update the "room" of the house by using the update() method:

house.update({"rooms": 3})
print(house)

house.update({"type": "3 storey building"})
print(house)

# Removing Items
# There are several methods to remove items from a dictionary:
# The pop() method removes the items with the specified key name:

house.pop("type")
print(house)

# The popitem() method removes the last inserted item
house.popitem()
print(house)

# The del keyword removes the item with the specified key name:
print(vehicle)

del vehicle["brand"]

print(vehicle)

# The del keyword can also delete the dictionary completely

del vehicle

# print(vehicle) # this will cause an error because "vehicle" no longer exist.

# The clear() method empties the dictionary
print(car)

car.clear()

print(car)

car["brand"] = "Lexus"
car["model"] = "RX 350"
car["year"] = "2024"
car["color"] = "black"
print(car)

# Copy a Dictionary
# dic1 = dic2 -- this wont work
# The copy() method

thisdict = {
    "name": "Emma",
    "courses": ["HTML", "CSS", "JAVASCRIPT", "PYTHON"]
}

print(thisdict)

mydict = thisdict.copy()

print(mydict)

thisdict["courses"].append("SQL")
print(thisdict)
print(mydict)

# Nested Dictionaries

myFamily = {
    "child1": {
        "name": "Emma",
        "year": 1999
    },

    "child2": {
        "name": "Femi",
        "year": 2004
    },

    "child3": {
        "name": "maro",
        "year": 2008
    }
}

print(myFamily)


child1 = {
    "name": "Emma",
    "year": "1999"
}

child2 = {
    "name": "Femi",
    "year": 2004
}

child3 = {
    "name": "maro",
    "year": 2008
}

myFamily2 = {
    "child1": child1,
    "child2": child2,
    "child3": child3,
}


# Access items in Nested Dictionary
print(myFamily["child2"]["name"])

# Dictionary Methods
# clear(): Removes all the elements from a dictionary
# copy(): Returns a copy of the dictionary
# fromkeys(): Returns a dictionary with the specified keys and value
# get(): Returns the value of the specified key
# items(): Returns a list containing
# keys(): Returns a list containing the dictionary's key
# pop(): Removes the element with the specified key
# popitems(): Removes the last inserted key-value pair
