def most_frequent_chars(string):
    char_count = {}

    for char in string:
        if char != ' ':  # Ignore spaces
            char_count[char] = char_count.get(char, 0) + 1

    # Find the maximum frequency
    max_count = max(char_count.values())

    # Find all characters with the highest frequency
    most_frequent = [char for char in char_count if char_count[char] == max_count]

    return most_frequent, max_count

def main():
    while True:
        string = input('Enter a string: ').lower()
        chars, count = most_frequent_chars(string)
        print(f'The most frequent character(s) in "{string}": {", ".join(chars)} (appears {count} times).')

        while True:
            choice = input('Do you want to continue (y/n)? ').strip().lower()
            if choice in ('n', 'no'):
                print('Thanks for using our program!')
                return
            elif choice in ('y', 'yes'):
                break
            else:
                print('Please answer with "y" or "n".')

if __name__ == '__main__':
    main()
