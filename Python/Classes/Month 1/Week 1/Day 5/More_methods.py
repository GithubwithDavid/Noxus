
#? .split()
#* The split() method splits a string into a list.
# For example:
text = "My name is John"
print(text.split()) # Output: ['My', 'name', 'is', 'John']

# TODO: you can also specify the separator
text = "Banana, Apple, Cherry"
print(text.split(", ")) # Output: ['Banana', 'Apple', 'Cherry']

#? .join()
#* The join() method takes all items in an iterable and joins them into one string.
# For example:
text = ["My", "name", "is", "John"]
print(" ".join(text)) # Output: My name is John

#? .count()
#* The count() method returns the number of times a specified value appears in the string.
# For example:
text = "My name is John"
print(text.count("n")) # Output: 2

#? ,startswith()
#* The startswith() method returns True if the string starts with the specified value, otherwise False.
# For example:
text = "My name is John"
print(text.startswith("My")) # Output: True

#? .endswith()
#* The endswith() method returns True if the string ends with the specified value, otherwise False.
# For example:
text = "My name is John"
print(text.endswith("John")) # Output: True

#? .isalpha()
#* The isalpha() method returns True if all the characters are alphabet letters (a-z). It will give error if there is a space or a number.
# For example:
text = "MynameisJohn"
print(text.isalpha()) # Output: True

#? .isalnum()
#* The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
# For example:
text = "MynameisJohn123"
print(text.isalnum()) # Output: True

#? .isnumeric()
#* The isnumeric() method returns True if all the characters are numeric (0-9).
# For example:
text = "123"
print(text.isnumeric()) # Output: True

#? .islower()
#* The islower() method returns True if all the characters are in lower case.
# For example:
text = "my name is john"
print(text.islower()) # Output: True

#? .isupper()
#* The isupper() method returns True if all the characters are in upper case.
# For example:
text = "MY NAME IS JOHN"
print(text.isupper()) # Output: True

#? .istitle()
#* The istitle() method returns True if the string follows the rules of a title.
# For example:
text = "My Name Is John"
print(text.istitle()) # Output: True

#? .isspace()
#* The isspace() method returns True if all the characters in the string are whitespaces.
# For example:
text = " "
print(text.isspace()) # Output: True

#? .zfill()
#* The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
# For example:
text = "50"
print(text.zfill(5)) # Output: 00050

#! Escape characters:
#* Escape characters are used to insert characters that are illegal in a string.
# For example:
text = "We are the so-called \"Vikings\" from the north."
print(text) # Output: We are the so-called "Vikings" from the north.

#? \n
#* The \n escape character is used to insert a new line.
# For example:
text = "Hello\nWorld"
print(text) # Output: Hello
# World

#? \t
#* The \t escape character is used to insert a tab.
# For example:
text = "Hello\tWorld"
print(text) # Output: Hello   World

# TODO: These escape sequences are mostly used in the print() function. All other are not usually used in the print() function.


