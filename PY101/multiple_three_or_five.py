
'''
Input: int
Output: return the sum of all numbers between 1 and int input that are multiples of three or five
Rules: numbers must be multiple of three or five inclusive
Mental model of the problem (optional): list comprehension of range 1,int if number is divisible by three or five
Examples/Test Case:
Data Structures:
Algorithm: 
Code with Intent:

'''

def multisum(int):
    multiples = set()
    for num in range (0,int+1,3):
        multiples.add(num)
    for num in range (0,int+1,5):
        multiples.add(num)
    return sum(multiples)

print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)