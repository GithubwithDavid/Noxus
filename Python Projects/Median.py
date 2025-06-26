from typing import List
class Solution:
    def find_median(self, num1 : List[int], num2 : List[int]) -> float:
        numbers = num1 + num2
        numbers.sort()
        n = len(numbers)
        if n % 2 == 1:
            median = float(numbers[n // 2])
        else:
            diff1 = numbers[n // 2 - 1]
            diff2 = numbers[n // 2]
            median = (diff1 + diff2) / 2
        return round(median, 5) 

if __name__ == '__main__':
    num1 = list(map(int, input().split()))
    num2 = list(map(int, input().split()))
    Median = Solution()
    median = Median.find_median(num1, num2)
    print(median)