# Worksheet 1.2: Task 2 Solution

import sys

sequence = input()
from util import read_numbers
numbers = read_numbers()

Minimum = min(numbers)
print(f"{Minimum} is minimum")
Maximum = max(numbers)
print(f"{Maximum} is maximum")
Mean = sum(numbers) / len(numbers)
print(f"{Mean} is mean")

numbers.sort()
length = len(numbers)
if length % 2 == 1:
    Median = numbers[length // 2]
else:
    Median = numbers([length // 2 - 1] + [length // 2])/ 2
print(f"{Median} is median")

if len(numbers) == 0:
    print("Error: no numbers provided", File=sys.stderr)
    sys.exit(1)



