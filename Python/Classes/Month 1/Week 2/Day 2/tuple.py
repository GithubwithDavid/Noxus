
#! So, what is a tuple?
#? A tuple is an ordered collection of items, similar to a list,

#! Key differences between tuples and lists:
#? 1. Tuples are immutable, which means that once a tuple is created, its contents cannot be changed.
#? 2. Tuples are defined using parentheses () instead of square brackets [].

#! Some more key differences:
#? 1. Tuples are faster than lists.
#? 2. Tuples are more memory efficient than lists.
#? 3. Allows duplicate values.
#? 4. Maintains insertion order.
#? 5. Supports indexing and slicing.

#! Creating a tuple:
#? We can create a tuple by using parentheses () or the tuple() function.

empty_tuple = ()
fruits = ("apple", "banana", "cherry") # Tuple with same data type
mixed_tuple = ("apple", 1, True, 4.5) # Tuple with different data types
numbers = tuple([1, 2, 3, 4, 5]) # We can also use the tuple() function to create a tuple from an iterable.

# TODO: You must add a comma after the first element of the tuple. Otherwise, it will be considered as a string.
# For example:
not_a_tuple = ("apple") # This is a string, not a tuple.
single_element_tuple = ("apple",) # This is a tuple.
print(type(not_a_tuple)) # Output: <class 'str'>
print(type(single_element_tuple)) # Output: <class 'tuple'>

#! Methods in tuples:

#! count()
#? The count() method returns the number of times a specified value appears in the tuple.
# For example:
fruits = ("apple", "banana", "cherry", "apple", "cherry")
print(fruits.count("apple")) # Output: 2

#! index()
#? The index() method returns the position of the first occurrence of the specified value.
# For example:
fruits = ("apple", "banana", "cherry", "apple", "cherry")
print(fruits.index("apple")) # Output: 0

#! len()
#? The len() function returns the number of elements in a tuple.
# For example:
fruits = ("apple", "banana", "cherry", "apple", "cherry")
print(len(fruits)) # Output: 5

#! max() and min()
#? The max() function returns the largest item in an iterable.
#? The min() function returns the smallest item in an iterable.
# For example:
numbers = (1, 2, 3, 4, 5)
print(max(numbers)) # Output: 5
print(min(numbers)) # Output: 1

#! sum()
#? The sum() function returns the sum of all items in an iterable.
# For example:
numbers = (1, 2, 3, 4, 5)
print(sum(numbers)) # Output: 15

#! tuple()
#? The tuple() function converts a list or a string into a tuple.
# For example:
list_to_tuple = tuple([1, 2, 3, 4, 5])
string_to_tuple = tuple("Hello, World!")
print(list_to_tuple) # Output: (1, 2, 3, 4, 5)
print(string_to_tuple) # Output: ('H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!')

#! Tuple unpacking:
#? Tuple unpacking is a feature that allows us to assign the elements of a tuple to multiple variables.
# For example:
fruits = ("apple", "banana", "cherry")
green, yellow, red = fruits
print(green) # Output: apple
print(yellow) # Output: banana
print(red) # Output: cherry

#? Unpacking with asterisk (*):
#? We can use the asterisk (*) to unpack the remaining elements of the tuple into a list.
# For example:
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
(green, yellow, *red) = fruits
print(green) # Output: apple
print(yellow) # Output: banana
print(red) # Output: ['cherry', 'orange', 'kiwi', 'melon', 'mango']

#! Tuple concatenation:
#? We can concatenate two tuples using the + operator.
# For example:
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print(tuple3) # Output: (1, 2, 3, 4, 5, 6)

#! Tuple repetition:
#? We can repeat a tuple using the * operator.
# For example:
tuple1 = (1, 2, 3)
tuple2 = tuple1 * 3
print(tuple2) # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

#! Tuple membership test:
#? We can check if a value exists in a tuple using the in keyword.
# For example:
fruits = ("apple", "banana", "cherry")
print("apple" in fruits) # Output: True
print("orange" in fruits) # Output: False

#! Tuple slicing:
#? We can slice a tuple using the slice operator [].
# For example:
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5]) # Output: ('cherry', 'orange', 'kiwi')
print(fruits[:5]) # Output: ('apple', 'banana', 'cherry', 'orange', 'kiwi')
print(fruits[2:]) # Output: ('cherry', 'orange', 'kiwi', 'melon', 'mango')
print(fruits[-5:-2]) # Output: ('cherry', 'orange', 'kiwi')

#! Reversing a tuple:
#? We can reverse a tuple using the reversed() function.
# For example:
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
reversed_fruits = tuple(reversed(fruits))
print(reversed_fruits) # Output: ('mango', 'melon', 'kiwi', 'orange', 'cherry', 'banana', 'apple')
# TODO: You can also use tuple[::-1] to reverse a tuple.

print(fruits[::-1]) # Output: ('mango', 'melon', 'kiwi', 'orange', 'cherry', 'banana', 'apple')

#! Exercise:
#? - Create a tuple of numbers and find the largest and smallest value.
#? - Create a tuple of fruits and check if "apple" is present using the in operator.
#? - Create a tuple and reverse its order using slicing.
#? - Unpack a tuple of 5 elements and store them in separate variables.
#? - Combine two tuples into one.




























