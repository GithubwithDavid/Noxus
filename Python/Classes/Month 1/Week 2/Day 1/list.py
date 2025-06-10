#* What is a list?
#? A list in Python is an ordered collection of items that can store multiple data types.

#* Properties of a list
#? - Lists are mutable → You can change their values after creation.
#? - Lists allow duplicate values.
#? - Lists maintain the insertion order.
#? - Items in a list are indexed → Starting from 0.

#* Creating a list

empty_list = [] # empty list
fruits = ['cherry', 'banana', 'mango'] # list with same data type
mixed_list = [9, 9.6, 'cherry', None, True] # list with mixed data types
numbers = list((1, 2, 3, 4)) # Creating list using list()

#* Methods
#! append()
#? Adds an element to the end of the list.

number_list = [1, 2, 3, 4, 5]
number_list.append(6)
print(number_list)

#! insert()
#? Inserts an element at a specific index.

number_list = [1, 2, 4, 5, 6, 7, 8, 9]
number_list.insert(2, 3)
print(number_list)

#! extend()
#? Adds the elements of an iterable (like a list or tuple) to the end of the list.

fruits_list = ['banana', 'cherry', 'mango']
more_fruits = ('apple', 'strawberry')  # Using tuple instead of list
fruits_list.extend(more_fruits)
print(fruits_list)
# TODO: Differentiate between extend() and append()

#! remove()
#? - Removes the first occurrence of a specified element.

fruits_list.remove('banana')
print(fruits_list)
# TODO: Now as we said that it removes the first occurence in a list. Actually we have already learnt that in list we can store duplicate values so if two data types of same value are there, then it will remove the first one in index order. 

number_list = [1, 2, 3, 3, 4, 5, 6, 7, 8, 9]
number_list.remove(3)
print(number_list)

#! pop()
#? - Removes and returns an element from a specific index (default is the last element).

fruits_list.pop()
print(fruits_list)
# TODO: We can also remove elements occuring in a specific index by writing the index number inside the pop.

#! clear()
#? - Removes all elements from the list.

fruits_list = ['apple', 'banana', 'cherry']
fruits_list.clear()
print(fruits_list)  
# Output: []

#! index()
#? - Returns the index of the first occurrence of an element.

fruits_list = ['apple', 'banana', 'cherry']
index = fruits_list.index('banana')
print(index)  
# Output: 1

#! count()
#? - Returns the number of times an element appears in the list.
fruits_list = ['apple', 'banana', 'cherry', 'banana']
count = fruits_list.count('banana')
print(count)  
# Output: 2

#! sort()
#? - Sorts the list in ascending order by default.

number_list = [3, 1, 4, 1, 5, 9]
sorted_numbers = sorted(number_list)  # Creates new sorted list
reversed_numbers = sorted(number_list, reverse=True)  # Creates new reverse sorted list
print(sorted_numbers)
print(reversed_numbers)

#! reverse()
#? - Reverses the order of the list.

fruits_list = ['apple', 'banana', 'cherry']
fruits_list.reverse()
print(fruits_list)  
# Output: ['cherry', 'banana', 'apple']

#! copy()
#? - Returns a shallow copy of the list.

from copy import deepcopy
fruits_list = ['apple', ['banana', 'plantain'], 'cherry']
shallow_copy = fruits_list.copy()  # or list(fruits_list)
deep_copy = deepcopy(fruits_list)  # Better for nested lists
print(deep_copy)

#! len()
#? - Returns the number of elements in the list.

fruits_list = ['apple', 'banana', 'cherry']
print(len(fruits_list))  
# Output: 3

#! sum(), max() and min()
number_list = [3, 1, 4, 1, 5, 9]
print(max(number_list))  # Output: 9
print(min(number_list))  # Output: 1
print(sum(number_list))

#! list()
#? - Converts an iterable to a list.

string = 'hello'
char_list = list(string)  # Already efficient, but could use list comprehension for filtering
filtered_chars = [c for c in string if c.isalpha()]  # Only letters
print(char_list)
print(filtered_chars)

#* Exercises:

#? 1. Create a list of your favorite fruits and print the second fruit. You can access the second fruit by using index number like char_list[1].
#? 2. Create a list of your favorite fruits and print the number of fruits in the list.
#? 3. Create a list of your favorite fruits and print the fruits in reverse order.
#? 4. Create a list of your favorite fruits and print the fruits in ascending order.
#? 5. Create a list of your favorite fruits and print the fruits in descending order.
#? 6. Write a program to add 7 fruits to a list entered by the user.
#? 7. Write a program to enter the marks of 6 students and display them in sorted order.


