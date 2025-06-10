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
        n = check('Enter a number: ')
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == 1 or i == n or j == 1 or j == n:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()
        choice = input('Do you want to continue (y/n): ').lower()
        if choice not in ['yes', 'y']:
            print('Thanks for using our program. ')
            break
    
if __name__ == '__main__':
    main()    