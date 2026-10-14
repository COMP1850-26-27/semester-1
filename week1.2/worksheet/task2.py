# Worksheet 1.2: Task 2 Solution

import sys
from util import read_numbers

numbers = read_numbers()

if len(numbers) == 0:
    print("Error: no numbers provided", File=sys.stderr)
    sys.exit(1)

Minimum = min(numbers)
print(f"Minimum = {Minimum}")
Maximum = max(numbers)
print(f"Maximum = {Maximum}")
Mean = sum(numbers) / len(numbers)
print(f"Mean = {Mean}")

numbers.sort()
length = len(numbers)
if length % 2 == 1:
    Median = numbers[length // 2]
else:
    Median = (numbers[length // 2 - 1] + [length // 2])/ 2
print(f"Median = {Median}")





