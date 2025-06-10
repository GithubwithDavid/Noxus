
#* OK, it is time for some new things to learn. You know we learnt about boolean data type.
#* I want to tell that True is equal to 1 and False is equal to 0. So, you can use them in mathematical operations. 
#? See this.
a = int(True)
b = int(False)
print(a, b)

#? Now, there is also a function to convert numbers into boolean
a = bool(1)
b = bool(0)
c = bool("Hello")
d = bool("")
print(a, b, c, d)

#? These are some values that appear as False
#! - 0 (integer)
#! - 0.0 (float)
#! - "" (empty string) 
#! - [] (empty list)
#! - {} (empty dictionary)
#! - set() (empty set)
#! - None

#? Everything else will be true

# TODO: You can also use logical operators on boolean.
print(True and False)
print(True or False)
print(not False)

#! Exercises: 
#? - Split "apple#banana#cherry" using 
#? - Count how many "l" are in "hello world".
#? - Use zfill() to make "42" five digits long.
#? - Check if 42 is greater than 21.
#? - Check if 'apple' exists in the list ['apple', 'banana', 'cherry'].
#? - Use and, or, and not together to create a single expression that evaluates to True.
#? - Use bool() to convert an empty list to a boolean value.