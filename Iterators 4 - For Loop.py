# Iterators - Exercise 4 🐍

"""
iterate each elements of `list1`,`tuple1`,`set1` and print them out 

for the `dict1` iterate all elements but only print the ones who are living on land
in the form of `x lives in y`
"""

list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":"land", "monkey":"land", "dog":"land","fish":"water"}

# iterating through list1:

print("*** From list1 ***")
for l in list1:
    print(l)

# iterating through tuple1:

print("*** From tuple1 ***")
for t in tuple1:
    print(t)

# iterating through set1:

print("*** From set1 ***")
for s in set1:
    print(s)

# iterating through dict1:

print("*** From dict1 ***")
for animal, place in dict1.items():
    if place == 'land':
        print(f"{animal} lives in {place}")