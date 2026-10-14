# Week 1.3, Additional work: Frequency Analysis

# Frequency analysis is a method of breaking certain ciphers which involves counting the frequency of letters/symbols
# because English has quite a clear distribution of letters, with spikes on common letters such as 'e', 'i' and 's'

# open and read the file 
# and count how many instances of each letter are in the program
# hint: use a dictionary!

# Additional hints:
# - You could handle the case where the file might not exist with try-except
# - You'll need to check each character to see if it's a letter
# - Dictionary pattern: if key exists, increment; if not, set to 1
# - Consider converting to lowercase for consistent counting


# checking
# code.txt
# letter frequency: please double check
# {'i': 5, 'n': 6, 'c': 1, 'l': 4, 'u': 2, 'd': 3, 'e': 3, 's': 1, 't': 4, 'o': 3, 'h': 2, 'm': 1, 'a': 1, 'p': 1, 'r': 4, 'f': 1, 'w': 1}

# story.txt
# letter frequency: please double check
# {'o': 7, 'n': 11, 'c': 2, 'e': 24, 'u': 5, 'p': 1, 'a': 15, 't': 14, 'i': 8, 'm': 2, 'f': 1, 'r': 8, 'w': 2, 'y': 2, 'l': 12, 'd': 10, 'h': 7, 'v': 3, 's': 5, 'g': 3}