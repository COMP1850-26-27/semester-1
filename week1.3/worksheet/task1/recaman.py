# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input


# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'

sequence = [0]
for k in range(1,L):
    last = sequence[-1]
    number = last - k

# You may wish to use further output for testing purposes while you develop your code

if number > 0 and number not in sequence:
   sequence.append(number)
else:
   sequence.append(last + k)

[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence