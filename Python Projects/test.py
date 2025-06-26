def num2words(n):
    units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if 0 <= n < 10: return units[n]
    elif 10 <= n < 20: return teens[n - 10]
    elif 20 <= n < 100 and n % 10 == 0: return tens[n // 10]
    elif 20 <= n < 100 and not n % 10 == 0: return tens[n // 10]+ " " + units[n % 10]
    else:
        return "Out of range"

if __name__ == '__main__':
    n = int(input())
    print(num2words(n))

