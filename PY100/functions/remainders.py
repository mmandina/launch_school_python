def remainders_3(numbers):
    return [number % 3 for number in numbers]

'''
Use this function to determine which of the following lists 
contains at least one number that is not evenly 
divisible by 3 (that is, the remainder is not 0):
'''

def contains_value_not_divisible_by_3(remaindersList):
    if any(remainder != 0 for remainder in remaindersList):
        return True
    return False

def check_number_lists(lists):
    results = []
    for list in lists: 
        remainders = remainders_3(list)
        results.append(contains_value_not_divisible_by_3(remainders))
    print(results)

numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []
check_number_lists([numbers_1,numbers_2,numbers_3,numbers_4])
