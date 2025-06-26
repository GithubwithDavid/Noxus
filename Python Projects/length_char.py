def check_num(prompt, string):
    while True:
        try:
            a = int(input(prompt))
            if not(a > len(string) or a <= 0):
                return a
            print('You can\'t the length greater than length of string or less than or equals to zero.')
        except ValueError:
            print('Please enter a string or a character.')

def find_subs(string, k):
    substrings = set()
    for i in range(len(string) - k + 1):
        substrings.add(string[i:i + k].lower())
    return substrings

def main():
    string = input('Enter a string: ')
    k = check_num('Enter the length of substrings: ',string)
    unique_substrings = find_subs(string, k) 
    print(f'The unique substrings in {string} are: {unique_substrings}.')

if __name__ == '__main__':
    main()