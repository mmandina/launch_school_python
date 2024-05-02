'''
Write a function, even_or_odd, that determines whether its argument is an even or odd number. 
If it's even, the function should print 'even'; otherwise, it should print 'odd'. 
Assume the argument is always an integer.
'''

def even_or_odd(num):
    print('even') if num % 2 ==0 else print('odd')

number = int(input('Enter a number:'))
even_or_odd(number)