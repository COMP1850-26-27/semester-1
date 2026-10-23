# Worksheet 1.2: Task 2 Solution
from util import read_numbers
import sys
numbers = read_numbers()
if len(numbers) == 0:
    sys.exit("Error: no numbers provided")
print("Minimum =", min(numbers))
print("Maximum =", max(numbers))
print("Mean =", sum(numbers) / len(numbers))
numbers.sort()
if len(numbers) % 2 == 0:
    median = (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
else:
    median = numbers[len(numbers) // 2]

print("Median =", median)
