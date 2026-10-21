# code example on slide 10
def test(x, intList):
    intList.append(x)
    return intList


list1 = [2, 4, 6, 8]
print(list1)             # [2, 4, 6, 8]
print(test(500, list1))  # [2, 4, 6, 8, 500]
print(list1)


# code example on slide 11
def test2(x, intList):
    temp_list2 = intList.copy()
    temp_list2.append(x)
    return temp_list2


list2 = [1, 2, 3, 4]
print(list2)             # [1, 2, 3, 4]
print(test2(5, list2))   # [1, 2, 3, 4, 5]
print(list2)             # [1, 2, 3, 4]
