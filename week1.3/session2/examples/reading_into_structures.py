# Week 1.3, Session 2: Reading data into a structure

with open("student_data.csv", "r") as f:
    # this creates a list of strings:
    data = f.readlines()

print(data)