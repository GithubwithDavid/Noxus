
#* Now, we will discuss about the input and output in Python.
#? SO, what is IO in Python?
#* IO stands for Input and Output. It is used to take input from the user and display the output on the console.
#* In Python, we have two functions for IO:
#? 1. input()
#? 2. print()

#* Let's input a number from the user and print it on the console.
a = input("Enter a number: ")
print(a)

# TODO: Input() is used to take input from the user. It always returns a string.
print(type(a))

#* You can use it without variable also.
input("Enter a number: ")
#! But the value will be lost as it is not stored in any variable.

#* let's discuss how it happened.
a = input("Enter a number: ") #* Now, you have to enter a number.
a = 5 #* Consider the value you entered is 5
print(a) #* It will print 5.

#* Now, let's see the same code without the input() function.
input("Enter a number: ") #* Now, you have to enter a number.
5 #* Consider the value you entered is 5
#! Now you can't call it because you don't have any variable to store it.

#* Now, let's talk about the output.
#? print() is used to print the output on the console. As We have already seen it in the previous examples.
#* There is a format method who is used widely.
print(f"Value of a is: {3+2}")

#! Class ends here.

#? Assignment: Write a program that takes your name and age as input and prints it on the console.