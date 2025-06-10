
#? So, what are operators?
#* Operators are special symbols in Python that carry out arithmetic or logical computation. The value that the operator operates on is called the operand.
#* For example:
a = 10 + 5 # Here, = and + are operators, 10 and 5 are operands. a is the variable where the result is stored. 

#! Types of Operators
#* Python language supports the following types of operators:
#? - Arithmetic Operators
#? - Comparison (Relational) Operators
#? - Assignment Operators
#? - Logical Operators
#? - Bitwise Operators
#? - Membership Operators
#? - Identity Operators

#! Arithmetic Operators
#* Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication etc.
#* For example:
a = 10
b = 5
print(a + b) # Addition
print(a - b) # Subtraction
print(a * b) # Multiplication
print(a / b) # Division
print(a // b) # Floor Division
print(a % b) # Modulus (Remainder)
print(a ** b) # Exponentiation

#! Now, there are some operators that will confuse you. Let's see them one by one.
#* Floor Division: The division of operands where the result is the quotient in which the digits after the decimal point are removed. But if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity). The division operator / returns a float value while // returns an integer value.
#* Modulus: The modulus operator % returns the remainder of the division of the number to the left by the number on its right. For example, 10 % 3 = 1 means 1 is the remainder when 10 is divided by 3.
#* Exponentiation: The exponentiation operator ** calculates the power of a number. For example, 2 ** 3 = 8 means 2 raised to the power of 3.

#! Comparison Operators
#* Comparison operators are used to compare values. It either returns True or False according to the condition.
#* For example:
a = 10
b = 5
print(a == b) # Equal to
print(a != b) # Not equal to
print(a > b) # Greater than
print(a < b) # Less than
print(a >= b) # Greater than or equal to
print(a <= b) # Less than or equal to

# TODO: These operators will give result in boolean values. True or False. We can store them in a variable and use them in if-else statements.
a = 5 + 3
b = 5 < 4
print(a)
print(b)

#! Logical Operators
#* Logical operators are the and, or, not operators.
#* For example:
a = True
b = False
print(a and b) # Logical AND
print(a or b) # Logical OR
print(not a) # Logical NOT

#! Let's figure out what these operators do.
#* Logical AND: If both the operands are true then condition becomes true. 
#* Logical OR: If any of the two operands are non-zero then condition becomes true.
#* Logical NOT: Used to reverse the logical state of its operand.
#? Also make truth table of these operators.

#! Assignment Operators
#* Assignment operators are used in Python to assign values to variables.
#* For example:
a = 10
b = 5

#* There are many assignment operators in Python, such as +=, -=, *=, /= etc.
#* For example:
a += b # a = a + b
a -= b # a = a - b
a *= b # a = a * b
a /= b # a = a / b
a %= b # a = a % b
a //= b # a = a // b
a **= b # a = a ** b

#! We will talk about other operators next time. 

#! Exercises:
#? 1. Write a program that will take two numbers from the user and print the sum, difference, product, division, floor division, and modulus of those numbers.