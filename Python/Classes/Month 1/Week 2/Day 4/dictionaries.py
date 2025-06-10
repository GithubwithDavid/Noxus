
#! Dictionaries
#? A dictionary in Python is an unordered collection of key-value pairs.
#? - Keys are unique identifiers for values.
#? - Values can be of any data type.
#? - Dictionaries are mutable.
#? - Keys must be immutable (e.g., strings, numbers, tuples).

#! Creating a dictionary
# You can create a dictionary using curly braces {} or the dict() constructor.

empty_dict = {} # Empty dictionary
person = {
    "name": 'John',
    'age': 20,
    'city': 'New York'
} # Dictionary with key-value pairs

#? Using the dict() constructor
person = dict(name='John', age=20, city='New York')
print(person)

#! Accessing values
# You can access values in a dictionary using the key.
print(person['name']) # Output: John
print(person['age']) # Output: 20

# TODO: If key doesn't exist, it will raise a KeyError.
# print(person['email']) # Output: KeyError: 'email'

#! get() method
# The get() method returns the value of the item with the specified key.
print(person.get('age')) # Output: 20

# TODO: If key doesn't exist, it will return None.
print(person.get('email')) # Output: None

# TODO: You can also specify a default value.
print(person.get('email', 'Not found')) # Output: Not found

#! update() method
# The update() method updates the dictionary with the key-value pairs from another dictionary.
person.update({'age': 21, 'email': 'john@example.com'})
print(person)
# TODO: If the key doesn't exist, it will add the key-value pair to the dictionary. But if the key exists, it will update the value.

#! setdefault() method
# The setdefault() method returns the value of the item with the specified key. If the key doesn't exist, it will add the key-value pair to the dictionary.
person.setdefault('age', 21)
print(person)

# TODO: If the key exists, it will return the value of the key.
person.setdefault('name', 'Jane') # Can't change the value of the key.
print(person)

#! keys() method
# The keys() method returns a view object that displays a list of all the keys in the dictionary.
print(person.keys()) # Output: dict_keys(['name', 'age', 'city', 'email'])

#! values() method
# The values() method returns a view object that displays a list of all the values in the dictionary.
print(person.values()) # Output: dict_values(['John', 21, 'New York', 'john@example.com'])

#! items() method
# The items() method returns a view object that displays a list of all the key-value pairs in the dictionary.
print(person.items()) # Output: dict_items([('name', 'John'), ('age', 21), ('city', 'New York'), ('email', 'john@example.com')])


#! pop() method
# The pop() method removes the item with the specified key.
person.pop('age')
print(person)

# TODO: If the key doesn't exist, it will raise a KeyError.
# person.pop('email') # Output: KeyError: 'email'

#! popitem() method
# The popitem() method removes the last item from the dictionary.
person.popitem()
print(person)

#! copy() method
# The copy() method returns a shallow copy of the dictionary.
person_copy = person.copy()
print(person_copy)

#! clear() method
# The clear() method removes all items from the dictionary.
person.clear()
print(person)

#! Exercises:
#? - Create a dictionary with at least 5 key-value pairs.
#? - Use get() to access a key that does not exist and set a default value.
#? - Update the dictionary with new key-value pairs using update().
#? - Remove an element using pop() and display the remaining dictionary.
#? - Try using setdefault() on an existing and a non-existing key.
