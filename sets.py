# Sets
# Sets are list with no duplicate entries.

# A set is a collection which is unordered, Unchangeable, and unindexed
this_set = {"apple", "banana", "cherry"}
print(this_set)

# Note: Sets are unordered, so you cannot be sure in which order the
# items will appear.

this_set2 = {"apple", "banana", "cherry", "apple", False, True, 0,1}
# Note: The value force and 0 are considered the same value in sets, and
# are treated as duplicates
print(this_set2)

print("My name is Larry and Larry is my name".split())
print(set("My name is Larry and Larry is my name".split()))

names = ["Jack", "Jill", "John", "Jack"]
print(names)
print(set(names))

myset = {"apple", "banana", "cherry"} # set
mylist = ["apple", "banana", "cherry"] # list
mytuple = ("apple", "banana", "cherry") # tuple
name = "Larry" # String Data
mydict = { # Dictionary
   "name": "Larry",
   "Age": 21,
}

print(type(mydict))

# You cannot access items in a set bt referring to an index or a key.
# But you can loop through the set items by using a for loop,
# or ask if a specified value is present in a set,

names = {"Divine", "Larry", "Ben", "Alex", "Arya"}
for x in names:
   print(x)

# check if "banana" is present in a set
this_set = ["apple", "banana", "cherry"]
print("banana" in this_set)

# Check if "banana" is NOT present in the set:
print("banana" not in this_set)

# Once a set is created
# You cannot change its items, but you can add new items.
# To add one item to a set use the add() method.

items = {"Body Lotion", "Toothpaste", "Tissue Paper"}
print(items)

items.add("Baby Oil")
print(items)

# To add items from another set into current set,
# use the update() method.
this_set = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
this_set.update(tropical)
print(this_set)
# Adding elements of a list to a set:
mylist = ["kiwi", "orange"]
this_set.update(mylist)
print(this_set)

# To remove an item in a set, use the remove() ,
# or discard() method.
this_set.remove("banana")
print(this_set)
this_set.discard("kiwi")
print(this_set)

# we can also use the pop() method to remove an item,
# but this method will remove a random item,
# so you cannot be sure what item that gets removed.
this_set.pop()
print(this_set)

# The clear() method empties the set
this_set.clear()
print(this_set)

# The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
# del thisset
print(thisset)

# JOIN SETS
# There are several ways to join two or more sets in python.

# The union()
# The update()
# The intersection()
# The difference()
# The symmetric difference()

# The Union() and update() methods joins all items from both sides.

# The union()
# The union() method returns a new set with all items from both sets.

set1 = {"a", "b", "c"}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3)

# You can | operator instead of the union() method, and you will get the same result.
set1 = {"a", "b", "c"}
set2 = {1,2,3}

set3 = set1 | set2
print(set3)

# joining multiple set with the union() method:
set1 = {"a","b", "c"}
set2 = {1,2,3}
set3 = {"John", "Elena"}
set4 = {"apple", "banana", "cherry"}

myset = set1.union(set2,set3,set4)
print(myset)

# When using the | operator, separate the set with more | operators:
myset2 = set1 | set2 | set3 | set4
print(myset2)

# join a set and a tuple
# The union() method allows you to join a set with other data types like
# lists or tuples
# The result will be a set
x = {"a", "b", "c"}
y = {1,2,3}
z = x.union(y)
print(z)

# The update() method inserts all items from one set into another
# The update() changes the original set, and does not return a new sets.

set1 = {"a","b", "c"}
set2 = {1,2,3}
set1.update(set2)

print(set1)
# note: Both union() and update() will exclude duplicate items.

# The intersection() method finds the elements that exist in
# both sets and return them as new set

staff = {"Jack", "John", "Arya", "Sansa"}
employees = {"Arya", "Sansa", "James"}
inter = staff.intersection(employees)
print(inter)

# The difference() methods get the elements that are
# in the first set but not in another

set1 = {1,2,3,4}
set2 = {3,4,5,6}
set3 = set1.difference(set2)
print(set3)

# The symmetric difference() removes the common elements between both sets

set1 = {1,2,3,4}
set2 = {3,4,5,6}
set3 = set1.symmetric_difference(set2)
print(set3)


# FROZENSET
# frozenset is an immutable version of a set.
# Like sets, it contains unique, unordered, unchangeable elements
# Unlike sets, elements cannot be added or removed from a frozenset

x = frozenset({"apple", "banana", "cherry"})
set1 = {1,2,3,4}
y = frozenset(set1)
print(y)
print(x)


