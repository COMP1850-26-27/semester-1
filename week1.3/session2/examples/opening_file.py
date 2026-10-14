# Week 1.3, Session 2: Open file to read

with open("student_data.csv", "r") as f: # opening 'student_data.csv' in read mode

    for line in f:   # files are iterable!
        print(line)  # you will see that there is a \n (newline) at the end of each line

        # you can use the string method .strip() to remove leading and trailing characters (whitespace by default)
        # print(line.strip())  