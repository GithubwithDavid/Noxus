
#! What are conditional statements?
#? Conditional statements are used to control the flow of execution based on certain conditions. They allow your program to execute specific blocks of code when certain conditions are met.

#* Python supports the following conditional statements:
#? - if statement
#? - if-else statement
#? - if-elif-else statement

#! if statement
#? The if statement is used to execute a block of code if a certain condition is true.
# For example:
if 10 > 5:
    print("10 is greater than 5")

#! if-else statement
#? The if-else statement is used to execute a block of code if a certain condition is true, and another block of code if the condition is false.
# For example:
if 10 > 5:
    print("10 is greater than 5")
else:
    print("10 is not greater than 5")

#! if-elif-else statement
#? The if-elif-else statement is used to execute a block of code if a certain condition is true, and another block of code if the condition is false.
# For example:
if 10 > 5:
    print("10 is greater than 5")
elif 10 < 5:
    print("10 is less than 5")
else:
    print("10 is equal to 5")

#! Short Hand if statement
#? The short hand if statement is used to execute a block of code if a certain condition is true.
# For example:
print("10 is greater than 5") if 10 > 5 else print("10 is not greater than 5")

#! Conditions with and, or and not
#? The and, or and not operators are used to combine multiple conditions.
# For example:
x = 7
y = 3

if x > 5 and y < 5:
    print("Both conditions are true")
# Output: Both conditions are true

if x > 5 or y > 5:
    print("At least one condition is true")
# Output: At least one condition is true

if not (x < 5):
    print("x is NOT less than 5")
# Output: x is NOT less than 5

#! Exercises
#? 1. Write a program to check if a number is positive, negative or zero.
#? 2. Write a program to check if a number is even or odd.
#? 3. Write a program to check if a number is divisible by 5 and 3.
#? 4. Write a program to check if a man is eligible to vote if his age is greater than or equal to 18.
#? 5. Write a program to find the largest number among 4 four numbers entered by the user
#? 6. Write a program to find out whether a student is passed or fails, if it requires total 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
#? 7. A spam comment is defined as a text containing following keywords:
# “Make a lot of money”
# “buy now”
# “subscribe this”
# “click this”
#? Write a program to detect these spams.
#? 8. Write a program to find whether a given username contains less than 10 characters or not.

