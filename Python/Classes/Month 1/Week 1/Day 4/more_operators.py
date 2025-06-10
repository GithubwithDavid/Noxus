
#* Now, we will talk about bitwise operators but first of all you have to know about binary numbers.
#? Bitwise operators are used to compare (binary) numbers. They are used to perform bit-level operations on (binary) numbers.

#* Bitwise operators are given:
#* & - AND
#* | - OR
#* ^ - XOR
#* ~ - NOT
#* << - Left Shift
#* >> - Right Shift

#! AND
#* The & operator returns 1 if both bits are 1, otherwise 0.
a = 10
b = 4
print(a & b) # 0

#! OR
#* The | operator returns 1 if any of the bits is 1, otherwise 0.
print(a | b) # 14

#! XOR
#* The ^ operator returns 1 if the bits are different, otherwise 0.
print(a ^ b) # 14

#! NOT
#* The ~ operator returns the complement of a number.
print(~a) # -11
#* It is calculated as -(a+1)

#! Left Shift
#* The << operator shifts the bits to the left by the specified number of places.
print(a << 1) # 20

#! Right Shift
#* The >> operator shifts the bits to the right by the specified number of places.
print(a >> 1) # 5

#* These are the bitwise operators. They are used to perform bit-level operations on (binary) numbers.

# TODO: If you want to write a number in binary, you can use the following code.
#* For example:
a = 10
print(bin(a)) # 0b1010

# or you can store it like that
a = 0b1010 # the 0 and 1 after the 0b are the binary numbers.
print(a) # 10

#? Now, let's talk about the identity operators.
#* Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.

#* Identity operators are given:
#! is
#! is not

#! is
#* The is operator returns True if both variables are the same object.
a = 10
b = 10
print(a is b) # True

#! is not
#* The is not operator returns True if both variables are not the same object.
print(a is not b) # False

#! Membership operators
#* Membership operators are used to test if a sequence is presented in an object.

#* Membership operators are given:
#! in
#! not in

#! in
#* The in operator returns True if a sequence with the specified value is present in the object.
a = [1, 2, 3, 4, 5] # This is a list. We will learn about it in upcoming chapters.
print(3 in a) # True

#! not in
#* The not in operator returns True if a sequence with the specified value is not present in the object.
print(6 not in a) # True

#! So, Now we have to move on to the next topic.

#! Exercises:
#? - Write a program to captalize the sentence "hello world".
#? - Write a program to convert the sentence "HELLO WORLD" to lowercase.
