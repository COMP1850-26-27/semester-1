
def func_1(lst_value): 
    ''' 
    write your docstring to explain the function 
    #a running total is created
    #for each value in the array '1st_value' it is added to the running total
    #a mean is created for each value in the array
    # takes the sum and divides it by each value in the list to return 
    ''' 

    sum = 0 
    num_of_value = len(lst_value) 
    for value in lst_value: 
    sum = sum + value 
    return sum/num_of_value 