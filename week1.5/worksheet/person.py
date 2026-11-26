# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name = "", birthday = "" ):
        self.name = name
        self.birthday = birthday



try:  
    self.name  = input("Enter name: ")
    self.birthday  = input("Enter birthday: ")
except:
    TypeError

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
