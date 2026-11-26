# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input


# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'

# Your code for the Recaman Sequence
sequence = [0]
k = 1
ak = 0

for x in range (L - 1):
  if (ak - 1 - k) > 0 and (ak - k) not in sequence:
    ak = ak - k 
  else:
    ak = ak + k
  k += 1
  sequence.append(ak)


# You may wish to use further output for testing purposes while you develop your code

[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence