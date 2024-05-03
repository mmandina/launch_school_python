
'''
Input: None
Output: return none, print odd numbers in range 1-99 inclusive with each on a separate line
Rules: Each number must be on its own line, 1 and 99 must be included
Mental model of the problem (optional)
Examples/Test Case:
Data Structures:
Algorithm: for odd in range 1 - 100, increment by 2
Code with Intent:

'''


def odd_numbers():
    for odd in range (1,100,2):
        print(odd)

odd_numbers()