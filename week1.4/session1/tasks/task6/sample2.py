# Week 4, Session 1: Task 3

# You are given function add_two_numbers. Your task is to inspect the code,
# and the run the program and observe the output.


def add_two_numbers(num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    return (num1 + num2)     # What happen if you remove the parenthesis ()?


# Check if the following lines produce the correct output
print(add_two_numbers(3, 4))
print(add_two_numbers(num1=3, num2=4))
print(add_two_numbers(3, num2=4))

# Why does the next line work?
print(add_two_numbers("3", "4"))

# What happens if you try this? Uncomment the code to find out.
# print(add_two_numbers("three", "four"))
