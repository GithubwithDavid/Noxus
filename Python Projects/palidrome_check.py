def palidrome_check(string):
    new_string = ''.join(char for char in string if char.isalnum())
    if new_string[::-1] == new_string:
        print(f'{new_string} is a palidrome.')
    else:
        print(f'{new_string} is not a palidrome.')
    
def main():
    while True:
        string = input('Enter a string: ').lower()
        palidrome_check(string)

        while True:
            choice = input('Do you want to continue (y/n): ').lower()
            if choice in ['no', 'n']:
                print('Thanks for using our program.')
                return
            elif choice in ['yes', 'y']:
                break
            else:
                print('Answer in Y or N.')

if __name__ == '__main__':
    main()
    
