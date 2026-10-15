# Worksheet 1.2: Task 1 Solution
import sys
grade = input("Enter grade: ")

if grade.isdecimal() == False:
    sys.exit("Error: Grade must be an integer between 0 and 100")
grade = int(grade)

if grade < 0 or grade > 100:
    sys.exit("Error: Grade must be an integer between 0 and 100")
if grade >= 70:
    print(grade, "is a Distinction")
elif grade >= 40:
    print(grade, "is a Pass")
else:
    print(grade, "is a Fail")
