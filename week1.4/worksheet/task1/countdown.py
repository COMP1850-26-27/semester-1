
def countdown(number): 
    '''  
    This recursive function takes a positive integer number  
    and counts the number down to zero printing each value. 
    ''' 
    def countdown(number):

        if number < 0:       # Base case (stops recursion)
            return
        print(number)        # Prints current number

        countdown(number - 1)
    print(number) 
    countdown(number-1) 