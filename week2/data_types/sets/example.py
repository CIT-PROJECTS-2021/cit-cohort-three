# The following programs will help you understand sets

fruits = {"apple", "banana", "cherry"}
print(fruits)

# Add an element to a set
fruits.add("orange")
print(fruits)

# Add multiple elements to a set
fruits.update(["orange", "mango", "grapes"])
print(fruits)

# Remove an element from a set
fruits.remove("orange")
print(fruits)

# Remove the last element from a set
fruits.pop()
print(fruits)


# Remove an element from a set if it is present in the set
fruits.discard("banana")
print(fruits)

# Remove all elements from a set
fruits.clear()
print(fruits)


# Delete a set
del fruits

john_likes = {"apple", "banana", "cherry"}
jane_likes = {"banana", "cherry", "orange"}

# Intersection of two sets
print(john_likes & jane_likes)

# Union of two sets
print(john_likes | jane_likes)

# Difference of two sets
print(john_likes - jane_likes)

# Symmetric difference of two sets
print(john_likes ^ jane_likes)


# Membership test
print("banana" in john_likes)
print("kiwi" in john_likes)

# printing elements of a set
for x in john_likes:
    print(x)

# Frozensets are immutable sets
fruits = frozenset(["apple", "banana", "cherry"])
print(fruits)

# we can use sets to remove duplicates from a list
_list = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]
print(list(set(_list)))
