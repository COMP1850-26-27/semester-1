"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.
try: every_month = int(input("How much do you want to save every month:") )
except ValueError: print("Invalid amount")

# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.

total_saved = every_month * 12
print(total_saved)

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).

interest = total_saved * 0.008
Final_amount = total_saved + interest 
print(f"Welcome to enter final amount is £{Final_amount:.2f}")

