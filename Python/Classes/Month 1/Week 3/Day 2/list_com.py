
#! List Comprehension
#? List comprehension is a compact way to create lists using a single line of code instead of using loops.
# Basic syntax: 
# new_list = [expression for item in iterable if condition]
#* expression: The expression that generates the elements of the new list.
#* item: The element of the iterable.
#* iterable: The iterable to iterate over.
#* condition: The condition to filter the elements of the iterable.

#! Creating a list with for loop
#? Using for loop (without list comprehension)
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

#? Using list comprehension
squares = [x**2 for x in range(10)]
print(squares)

#! Using list comprehension with condition
#? Using for loop (without list comprehension)
even_squares = []
for x in range(10):
    if x % 2 == 0:
        even_squares.append(x**2)
print(even_squares)

#? Using list comprehension
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)

#! Using if else in list comprehension
#? Using for loop (without list comprehension)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_even = []
for x in numbers:
    if x % 2 == 0:
        odd_even.append("even")
    else:
        odd_even.append("odd")
print(odd_even)

#? Using list comprehension
odd_even = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(odd_even)

#! Nested list comprehension
#? Using for loop (without list comprehension)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = []
for i in range(len(matrix)):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)

#? Using list comprehension
transposed = [[row[i] for row in matrix] for i in range(len(matrix))]
print(transposed)

#! List Comprehesions with functions 
#? Using for loop (without list comprehension)
def square(x):
    return x**2
squares = []
for x in range(10):
    squares.append(square(x))
print(squares)

#? Using list comprehension
squares = [square(x) for x in range(10)]
print(squares)

#! Dictionary Comprehension
#? Using for loop (without dictionary comprehension)
squares = {}
for x in range(10):
    squares[x] = x**2
print(squares)

#? Using dictionary comprehension
squares = {x: x**2 for x in range(10)}
print(squares)

#! Set Comprehension
#? Using for loop (without set comprehension)
squares = set()
for x in range(10):
    squares.add(x**2)
print(squares)

#? Using set comprehension
squares = {x**2 for x in range(10)}
print(squares)

#! Generator Comprehension
#? Using for loop (without generator comprehension)
squares = (x**2 for x in range(10))
for x in squares:
    print(x)

#? Using generator comprehension
squares = (x**2 for x in range(10))
print(squares)

#! List Comprehension with if else
#? Using for loop (without list comprehension)











