import math
def check(prompt):
    while True:
        try:
            a = int(input(prompt))
            if 0 < a:
                return a
            print('Please enter a positive integer.')
        except ValueError:
            print('You have entered a character or string. Please try again.')

find_cube = lambda x : x**3
number = check('Enter a number: ')
cube = find_cube(number)
print(f'Cube of {number}: {cube}.')

