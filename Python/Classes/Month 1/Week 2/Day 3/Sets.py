
#! What is a set?
#? A set is an unordered collection of unique elements.

#! Key points about sets:
#? 1. Sets are unordered.
#? 2. Sets are unindexed.
#? 3. No duplicate elements are allowed.
#? 4. Supports mathematical operations like union, intersection, difference, etc.

#! Creating a set:
#? We can create a set using the set() function or by simply enclosing a list of elements in curly braces.

empty_set = set() # Empty set (must use set() to create an empty set - {} creates a dictionary)
fruits = {"apple", "banana", "cherry"} # Set of fruits

#? Using set() to create a set from a list:
numbers = set([1, 2, 3, 4, 5])
print(numbers) # Output: {1, 2, 3, 4, 5}

# TODO: The duplicates are not allowed in a set.
fruits = {"apple", "banana", "cherry", "apple"}
print(fruits) # Output: {'apple', 'banana', 'cherry'}

#! Methods

#? add()
#* This method adds an element to the set.

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits) # Output: {'apple', 'banana', 'cherry', 'orange'}
# TODO: The new element is added to the set, but the order of the elements is not guaranteed. Also remember that if an element already exists, it will not be added again.

#? clear()
#* This method removes all elements from the set.

fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits) # Output: set()

#? update()
#* This method updates the set with the elements from another set.

fruits = {"apple", "banana", "cherry"}
fruits.update(["orange", "mango", "grapes"])
print(fruits) # Output: {'apple', 'banana', 'cherry', 'orange', 'mango', 'grapes'}

#? remove()
#* This method removes an element from the set.

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits) # Output: {'apple', 'cherry'}

# TODO: If the element is not found, remove() will raise an error.

#? discard()
#* This method removes an element from the set.

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits) # Output: {'apple', 'cherry'}

# TODO: If the element is not found, discard() will not raise an error.

#? pop()
#* This method removes the last element from the set.

fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits) # Output: {'banana', 'cherry'}

# TODO: The pop() method removes a random element from the set.

#? union()
#* This method returns a new set with all elements from both sets.

fruits = {"apple", "banana", "cherry"}
fruits2 = {"orange", "mango", "grapes"}
new_fruits = fruits.union(fruits2)
print(new_fruits) # Output: {'apple', 'banana', 'cherry', 'orange', 'mango', 'grapes'}

# TODO: The union() method returns a new set with all elements from both sets.

#? intersection()
#* This method returns a new set with elements that are in both sets.

fruits = {"apple", "banana", "cherry"}
fruits2 = {"orange", "mango", "apple"}
new_fruits = fruits.intersection(fruits2)
print(new_fruits) # Output: {'apple'}

# TODO: The intersection() method returns a new set with elements that are in both sets.

#? difference()
#* This method returns a new set with elements that are in the first set but not in the second set.

fruits = {"apple", "banana", "cherry"}
fruits2 = {"orange", "mango", "apple"}
new_fruits = fruits.difference(fruits2)
print(new_fruits) # Output: {'banana', 'cherry'}

# TODO: The difference() method returns a new set with elements that are in the first set but not in the second set.

#? symmetric_difference()
#* This method returns a new set with elements that are in either set but not in both.

fruits = {"apple", "banana", "cherry"}
fruits2 = {"orange", "mango", "apple"}
new_fruits = fruits.symmetric_difference(fruits2)
print(new_fruits) # Output: {'banana', 'cherry', 'orange', 'mango'}

# TODO: The symmetric_difference() method returns a new set with elements that are in either set but not in both.

#? issubset()
#* This method returns True if all elements of a set are in another set.

fruits = {"apple", "banana", "cherry"}
fruits2 = {"orange", "mango", "apple"}
print(fruits.issubset(fruits2)) # Output: False

# TODO: The issubset() method returns True if all elements of a set are in another set.

#? issuperset()
#* This method returns True if all elements of a set are in another set.

fruits = {"apple", "banana", "cherry"}
fruits2 = {"orange", "mango", "apple"}
print(fruits.issuperset(fruits2)) # Output: False

# TODO: The issuperset() method returns True if all elements of a set are in another set.

#? isdisjoint()
#* This method returns True if two sets have no elements in common.

fruits = {"apple", "banana", "cherry"}
fruits2 = {"orange", "mango", "grapes"}
print(fruits.isdisjoint(fruits2)) # Output: True

# TODO: The isdisjoint() method returns True if two sets have no elements in common.

#? copy()
#* This method returns a shallow copy of the set.

fruits = {"apple", "banana", "cherry"}
new_fruits = fruits.copy()
print(new_fruits) # Output: {'apple', 'banana', 'cherry'}

#? Exercise:
#? - Create two sets and find their intersection.
#? -Create two sets and get the symmetric difference.
#? -Create a set and try adding a duplicate value — what happens?
#? -Create two sets and check if one is a subset of the other.