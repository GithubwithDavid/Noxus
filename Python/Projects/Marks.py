def check(prompt):
    while True:
        try:
            a = int(input(prompt))
            if 0 <= a <= 100:
                return a
            print('You have entered wrong marks. Please try again.')
        except ValueError:
            print('You have entered a character or string. Please try again.')

def main():
    while True:
        Subjects = ['English', 'Urdu', 'Math']
        marks = [check(f'Enter your {i} Marks: ') for i in Subjects]
        total = sum(marks)
        percent = (total / 300) * 100
        S_grade = ['Pass' if mark >= 33 else 'Fail' for mark in marks]
        total_grade = 'Pass' if percent >= 40 else 'Fail'
        print(f'''Your result is given below:
            English: Marks = {marks[0]}, Percentage = {marks[0]}%, Grade = {S_grade[0]},
            Urdu: Marks = {marks[1]}, Percentage = {marks[1]}%, Grade = {S_grade[1]},
            Math: Marks = {marks[2]}, Percentage = {marks[2]}%, Grade = {S_grade[2]},
            Total: Marks = {total}, Percentage = {percent:0.2f}%, Grade = {total_grade}''')
        
        choice = input('Do you want to continue (y/n): ').lower()
        if choice not in ['yes', 'y']:
            print('Thanks for using our program')
            break

if __name__ == '__main__':
    main()
