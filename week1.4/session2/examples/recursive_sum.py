# code example on slide 27
def recursive_sum_list(a):
    """
    This function recursively calls itself to calculate the sum
    of all numbers in a list. For simplisity, validity check for
    numbers is not included here.
    """

    # The base case
    if len(a) == 0:
        return 0
    # To combine sub-problems together
    else:
        return a[0] + recursive_sum_list(a[1:])


print(recursive_sum_list([1, 3, 5, 7, 9, 11]))   # 36
print(recursive_sum_list([10, 4, 56]))		       # 70


# code example on slide 28
def sum_list(a):
    sum = 0
    for number in a:
        sum = sum + number
    return sum
