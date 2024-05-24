'''Write a program that asks the user to enter an integer greater than 0, 
then asks whether the user wants to determine the sum or the product of all 
numbers between 1 and the entered integer, inclusive.'''


def sum_or_product():
    integer = int(input('Please enter an integer greater than 0: '))
    if integer <=0:
        raise Exception('integer must be greater than 0')

    sum_or_product = input('Enter "s" to compute the sum, or "p" to compute the product. ')
    if sum_or_product != 's' and sum_or_product != 'p':
        raise Exception('Only arguments of "s" and "p" are accepted')
        
    if sum_or_product == 's':
        sum = 0
        for num in range (1,integer+1):
            sum += num
        print(sum)
    
    if sum_or_product == 'p':
        prod = 1
        for num in range (1,integer+1):
            prod = prod * num
        print(prod)

sum_or_product()
