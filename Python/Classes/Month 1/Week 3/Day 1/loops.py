
#! Loops
#? Loops are used to repeat a block of code multiple times until a condition is met.
#? Python supports two main types of loops:
#* for loop → Used to iterate over a sequence (like a list, tuple, string, etc.)
#* while loop → Repeats until a condition becomes False

#! for loop
#? The for loop is used to iterate over a sequence (like a list, tuple, string, etc.)
# For example:
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

#? Using range() function
#* The range() function is used to generate a sequence of numbers.
# in range(start, stop, step)
# start is the starting number of the sequence. (default is 0)
# stop is the ending number of the sequence. (exclusive)
# step is the difference between the numbers in the sequence. (default is 1)

for i in range(1, 10, 2):
    print(i)

#? Loop through a string
#* You can loop through a string using a for loop.
# For example:
for x in "banana":
    print(x)

#? Loop through a dictionary
#* You can loop through a dictionary using a for loop.
# For example:
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

for x in person:
    print(person.get(x))

#! While loop
#? The while loop keeps executing as long as the condition is True.
# For example:
i = 1
while i < 6:
    print(i)
    i += 1

#! The break statement
#* The break statement is used to stop the loop.
# For example:
for x in range(10):
    if x == 5:
        break
    print(x)

#! The continue statement
#* The continue statement is used to skip the current iteration of the loop.
# For example:
for x in range(10):
    if x == 5:
        continue
    print(x)

#! else statement
#* The else statement is used to execute a block of code when the loop is finished.
# For example:
for x in range(10):
    print(x)
else:
    print("Finally finished!")

# TODO: If the loop is exited using break, the else block won't execute:

#! Nested loops
#* You can use a loop inside another loop.
# For example:
for x in range(10):
    for y in range(10):
        print(x, y)

#! pass statement
#* The pass statement is used to do nothing.
# For example:
for x in range(10):
    pass #* This is used to avoid getting an error when the loop is empty.

#! Infinite loop
#* An infinite loop is a loop that never ends.
# For example:
# x = 1
# while True:
#     print(x)
#     x += 1

# TODO: To avoid infinite loop, we can use the break statement. You can use CTRL+C to stop the loop.

#! Looping with zip() function
#* The zip() function is used to combine two lists into a single list of tuples.
# For example:
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for x, y in zip(list1, list2):
    print(x, y)

# TODO: The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together.







