
#* Now, we will learn about the methods of each data types.

#! Int Methods
#* Int methods are used to perform operations on integers.
# TODO: I think there is only one method for integers that is useful for us.

#? .bit_length()
#* The bit_length() method returns the number of bits required to represent an integer in binary, excluding the sign and leading zeros.
a = 10
print(a.bit_length()) # 4

#! Float Methods
#* Float methods are used to perform operations on floating-point numbers.

# TODO: Now, we have a method to know that the number is float, integer or string.
#? .is_integer()

#* The is_integer() method returns True if the number is integer or float.
a = 10.0
b = 10.5
print(a.is_integer()) # True
print(b.is_integer()) # False

#! String Methods
#* String methods are used to perform operations on strings.

# TODO: String methods are very useful for us. They will help us very much in the future.

#? .upper()
#* The upper() method returns the string in uppercase.
a = "hello"
print(a.upper()) # HELLO

#? .lower()
#* The lower() method returns the string in lowercase.
a = "HELLO"
print(a.lower()) # hello

#? .capitalize()
#* The capitalize() method returns the string with the first character capitalized.
a = "hello world"
print(a.capitalize()) # Hello world

#? .title()
#* The title() method returns the string with the first character of each word capitalized.
a = "hello world"
print(a.title()) # Hello World

#? .strip()
#* The strip() method returns the string with leading and trailing whitespaces removed.
a = "  hello world  "
print(a.strip()) # hello world

#? .lstrip()
#* The lstrip() method returns the string with leading whitespaces removed.
print(a.lstrip()) # hello world

#? .rstrip()
#* The rstrip() method returns the string with trailing whitespaces removed.
print(a.rstrip()) # hello world

#? .find()
#* The find() method returns the index of the first occurrence of the substring in the string.
a = "hello world"
print(a.find("world")) # 6
# TODO: If the substring is not found, it returns -1.
print(a.find("worlds")) # -1
# TODO: We have to learn about index of the string.

#? .index()
#* The index() method returns the index of the first occurrence of the substring in the string.
a = "hello world"
print(a.index("world")) # 6
# TODO: If the substring is not found, it raises a ValueError.
# print(a.index("worlds")) # ValueError: substring not found

#? .replace()
#* The replace() method replaces the substring with another substring in the string.
a = "hello world"
print(a.replace("world", "python")) # hello python
