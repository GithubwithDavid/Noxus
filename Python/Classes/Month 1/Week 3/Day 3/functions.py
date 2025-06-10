
#! Functions
#? Functions in Python allow us to reuse code by defining a block of statements that can be executed when needed.

#! Defining a function
# TODO: A function is defined using the def keyword.

def function_name(parameters):
    # Code inside the function
    # return value  # (optional)
    pass

# For Example:
def greet():
    print("Hello, World!")

greet()  # Output: Hello, World!

#! Parameters and Arguments and Return Statement
# TODO: Parameters are the variables listed inside the parentheses in the function definition.
# TODO: Arguments are the values passed to the function during the function call.
# TODO: The return statement is used to return a value from the function.

def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8

#! Default Parameters
# TODO: Default parameters are parameters that are given a default value.

def greet(name="World"):
    print(f"Hello, {name}!")

greet()  # Output: Hello, World!
greet("John")  # Output: Hello, John!

#! Keyword Arguments
# TODO: Keyword arguments are arguments that are passed to the function with the parameter name.

def greet(name="World", age=20):
    print(f"Hello, {name}! You are {age} years old.")

greet(age=25, name="John")  # Output: Hello, John! You are 25 years old.

#! Arbitrary Arguments
# TODO: Arbitrary arguments are arguments that allow us to pass a variable number of arguments to the function.

def add(*args):
    return sum(args)

print(add(1, 2, 3, 4, 5))  # Output: 15

#! Arbitrary Keyword Arguments
# TODO: Arbitrary keyword arguments are arguments that allow us to pass a variable number of keyword arguments to the function.

def greet(**kwargs):
    print(kwargs)

greet(name="John", age=25)  # Output: {'name': 'John', 'age': 25}

#! Function with a list as an argument
# TODO: A function can take a list as an argument and return a list.

def square_list(numbers):
    return [x**2 for x in numbers]

print(square_list([1, 2, 3, 4, 5]))  # Output: [1, 4, 9, 16, 25]

#! Lambda Functions
# TODO: Lambda functions are small, anonymous functions that can have any number of parameters.

square = lambda x: x**2

print(square(5))  # Output: 25


