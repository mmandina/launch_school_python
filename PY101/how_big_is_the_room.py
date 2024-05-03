'''
Input: ifloat width, float length both in meters
Output: return none, print the area in square meters and square feet
Rules: must be in square meters and square feet
Mental model of the problem (optional)
Examples/Test Case: [10,2] 20, 20*10.7639 square feet
Data Structures:
Algorithm: for odd in range 1 - 100, increment by 2
Code with Intent:
'''

def how_big_is_the_room(length,width):
    print('Square Meters: ',length*width)
    print('Square Feet:',length*width*10.7639)

how_big_is_the_room(2,1)