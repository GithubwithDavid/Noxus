def unique_char(string):
    char_dict = {}
    for char in string:
        if char != ' ':
            char_dict[char] = char_dict.get(char, 0) + 1
    
    return [char for char in string if char_dict[char] == 1]

def main():
    string = input('Enter a string: ')
    result = unique_char(string)
    print(f'The unique character(s) in {string} is/are: {" ".join(result)}')

if __name__ == '__main__':
    main()
