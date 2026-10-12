# Week 1.3, Session 2: Basic data cleaning

with open("student_data.csv", "r") as f:
    data = f.readlines()

print(data)
# this is a good use for list comprehensions:
data = [ line.strip().split(",") for line in data ]

'''
You can also use a for loop if you find list comprehensions hard to read:

# make a new list to hold the clean data
clean = []

for line in data:
    # remove the trailing newline character '\n'
    line = line.strip()

    # break each line up on the comma
    line = line.split(",")

    clean.append(line)

print(clean)

'''


print(data)