'''
Process the Problem	
Identify expected input and output
Make the requirements explicit
Identify rules
Mental model of the problem (optional)
Examples/Test Case
Data Structures:
Algorithm:
Code with Intent:

'''

def isOdd(int):
    absolute_value = abs(int)
    if absolute_value % 2 == 0:
        return True
    else:
        return False
    
print(isOdd(-3))
print(isOdd(3))
print(isOdd(2))
print(isOdd(-2))