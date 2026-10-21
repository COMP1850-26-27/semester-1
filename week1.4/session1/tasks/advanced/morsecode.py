"""
    This task assumes some experience with Python.

    You are given an incomplete function string_to_morse_code.
    Your task is to complete the function that returns the Morse code of
    a string. The input string consists of upper or lower case characters,
    digits, and special characters (e.g. comma, colon, apostrophe, period,
    question mark, and exclamation mark) as in mcode.

    Each character converted to Morse code is spaced with a blank space " ",
    except the last character. You can create additional functions to be
    called from this function.
"""


def string_to_morse_code(string):
    """
    Returns the Morse code of the string.
    """

    mcode = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
             'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
             'K': '-.-', 'L': '.-..', 'M': '--',   'N': '-.', 'O': '---',
             'P': '.--.', 'Q': '--.-', 'R': '.-.',  'S': '...', 'T': '-',
             'U': '..-', 'V': '...-', 'W': '.--',  'X': '-..-', 'Y': '-.--',
             'Z': '--..', ' ': ' ', '0': '-----', '1': '.----', '2': '..---',
             '3': '...--', '4': '....-',  '5': '.....',  '6': '-....',
             '7': '--...', '8': '---..',  '9': '----.',  '&': '.-...',
             "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
             ':': '---...', ',': '--..--', '=': '-...-',  '!': '-.-.--',
             '.': '.-.-.-', '-': '-....-', '+': '.-.-.',  '"': '.-..-.',
             '?': '..--..', '/': '-..-.'}


# test data

# .... . .-.. .-.. ---   .-- --- .-. .-.. -.. -.-.--
print(string_to_morse_code("Hello world!"))

# -- --- .-. ... .   -.-. --- -.. .
print(string_to_morse_code("morse code"))

# .-
print(string_to_morse_code("a"))             
