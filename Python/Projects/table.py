def check(prompt):
    while True:
        try:
            a = int(input(prompt))
            if a > 0:
                return a
            print('Please enter a positive integer.')
        except ValueError:
            print('You have entered a string or character. Try again')

def main():
    while True:
        n = check('Enter the number whose table do you want: ')
        r = check('How far do you want the table: ')
        for i in range(1, r + 1):
            print(f'{n} * {i} = {n*i}')
        
        choice = input('Do you want to continue (y/n): ').lower()
        if choice not in ['yes', 'y']:
            print('Thanks for using our program. ')
            break
if __name__ == '__main__':
    main()    