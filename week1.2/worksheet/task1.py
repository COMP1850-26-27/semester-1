# Worksheet 1.2: Task 1 Solution

import sys

grade = int(input())
if 0 <= grade <= 39:
    print(f"{grade} is a Fail")
elif 40 <= grade <= 69:
    print(f"{grade} is a Pass")
elif 70 <= grade <= 100:  
    print(f"{grade} is a Distinction")

if grade < 0 or grade > 100:
    print("Error: Grade must be an integer between 0 and 100")
    sys.exit(1)
