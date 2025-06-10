
#* What is a variable?
#? A variable is a container for a value, which can be of various types. One important thing about variable is that we can change its value during the program.
# TODO: You can give math examples.

#* Types of variables
#? There are different types of variables in Python, such as:
#? - int
#? - float
#? - string
#? - boolean

#! These are the most common types of variables in Python. There are more types of variables in Python, but these are the most common ones. We will discuss them in detail in the next lessons.

#* What is an int variable?
#? An int variable is a variable that stores an integer value. An integer value is a whole number, without a decimal point.
a = 5 
b = -10
#* You can store any integer value. Doesn't matter if it is positive or negative.

#* What is a float variable?
#? A float variable is a variable that stores a floating-point number. A floating-point number is a number that has a decimal point.
c = 5.5
d = -10.5 #* You can store any floating-point number. Doesn't matter if it is positive or negative.
expo = 2e3 #! You can also use scientific notation to represent floating-point numbers. It means 2 * 10^3.

#* What is a string variable?
#? A string variable is a variable that stores a sequence of characters. A string can contain letters, numbers, and special characters.
e = "Hello"

#! Now, there is a string type called multiline string. It is a string that can span multiple lines. You can create a multiline string by using three double quotes or three single quotes.
multiline_string = """This is a
multiline string""" # TODO: In normal strings, you can't use new lines. But in multiline strings, you can use new lines.
#* For example:
# a = "This is a normal string
# but this is a multiline string"

#! If you want to do that in a normal string, you can use the escape character \n.
normal_string = "This is a normal string\nbut this is a multiline string"

#* What is a boolean variable?
#? A boolean variable is a variable that stores a boolean value. A boolean value is either True or False.
f = True
g = False

#* How to print variables?
#? You can print variables using the print() function.
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#! Now, there is a function to know the type of a variable. It is the type() function. It returns the type of the variable.
print(type(a))
print(type(c))
print(type(e))
print(type(f))

#* Rules for naming variables
#? There are some rules for naming variables in Python:

#? - A variable name must start with a letter or an underscore (_).
#? - A variable name cannot start with a number.
#? - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _).
#? - Variable names are case-sensitive (age, Age, and AGE are three different variables).
#? - Variable names cannot contain spaces.
#? - Variable names should be descriptive (age is better than a).
#? - Variable names should be in lowercase (age is better than Age).
#? - Variable names should not be Python keywords (for example, if, else, while, etc.).
#? - Variable names should not be built-in functions (for example, print, input, len, etc.).
# TODO: Also give real life examples like naming persons.

#* Examples of valid variable names
#? - age
#? - Age
#? - AGE
#? - _age
#? - age1
#? - age_1

age = 1
Age = 2
AGE = 3

print(age, Age, AGE)

#* Examples of invalid variable names
#? - 1age
#? - age$
#? - age 1
#? - for
#? - print

#* For Example, This is an example of a code using variables. 
name = "David"
age = 25
print("My name is" , name , "and I am" , age , "years old.")

#* Exercises:
#? - Write a code and print your name and age using variables.
#? - Check the type of the variables you have created.


