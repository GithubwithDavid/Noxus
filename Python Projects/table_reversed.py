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
        print()  # Add spacing before table
        for i in range(r):
            print(f'{n} * {r-i} = {n*(r-i)}')
        print()  # Add spacing after table
        
        while True:
            choice = input('Do you want to continue (y/n): ').lower()
            if choice in ['yes', 'y']:
                break
            elif choice in ['no', 'n']:
                print('Thanks for using our program.')
                return
            else:
                print('Please enter "y" or "n"')
        
if __name__ == '__main__':
    main()    