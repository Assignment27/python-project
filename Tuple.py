# TUPLE
# A Tuple is a collection of ordered,in immutable element in python.
# its similar to a list, but you cant change "modify" the value once defined
# Tuples are created by placing element inside parenthesis ().

my_tuple = (10,20,30)
print(my_tuple)

# You can also have a Tuple without parenthesis using just commas

my_tuple = 10,20,30,40,50,60
print(my_tuple)

# Characteristic of Tuples
# Ordered: items has a fixed position
# in immutable: you cant change items after creation
# Allow duplicate
# can contain different data types

mixed_tuple =(1,"hello",True,3.5)
print(mixed_tuple)

# Tuple operations
# Length: len(my_tuple)
# Count: my_tuple.count(value)
# Index: my_tuple.index(value)
# Slicing: my_tuple.slicing(value)

example = (5,10,15,20,10)
print(len(example))
print(example.count(10))
print(example.index(15))
print(example[::-1])
print(example[0])

# Tuple unpacking
# You can assign tuple items to variables directly

a,b,c = (1,2,3)
print(a)
print(b)
print(c)

print(c+b)

Grade = (40,45,46,47,48,50)
grade1, grade2, grade3, grade4, grade5, grade6 = Grade
print(grade1)

# Nested Tuple

nested = ((1, 2), (3,4))
print(nested[1][1])
print(nested[0][1] )

# When to use Tuples
# When data should not change (e.g coordinates, constant settings)
# When you want faster performance.
# As dictionary keys (tuples are hashable, lists are not).

# tuple as dictionary keys
scores = {
    ("Alice", "Math"): 85,
    ("Bob", "Science"): 90,
    ("Alice", "Science"): 88
}

print(scores[("Bob", "Science")])
