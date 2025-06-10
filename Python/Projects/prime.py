def check(prompt):
    while True:
        try:
            a = int(input(prompt))
            if a >= 0:
                return a
            print('Please enter a positive integer.')
        except ValueError:
            print('You have entered a string or character. Please try again.')

def main():
    while True:
        n = check('Enter a number: ')
        flag = False
        if n == 0 or n == 1:
            print(f'{n} is not a prime number.')
        elif n > 1:
            for i in range(2, n):
                if n % i == 0:
                    flag = True
                    break
                
            if flag:
                print(f'{n} is not a prime number.')
            else:
                print(f'{n} is a prime number')
        
        choice = input('Do you want to continue (y/n): ').lower()
        if choice not in ['yes', 'y']:
            print('Thanks for using our program.')
            break

if __name__ == '__main__':
    main()