'''Create a function that takes 2 arguments, a list and a dictionary. 
The list will contain 2 or more elements that, when joined with spaces, 
will produce a person's name. The dictionary will contain two keys, "title" and 
"occupation", and the appropriate values. Your function should return a greeting 
that uses the person's full name, and mentions the person's title.
'''

# def greetings(list,dict):
#     name = ' '.join(list)
#     return f'Hello, {name}! Nice to have a {dict['title']} {dict['occupation']} around.'

# greeting = greetings(
#     ["John", "Q", "Doe"],
#     {"title": "Master", "occupation": "Plumber"},
# )


# print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.

# def greeting_yell():
#     name = input('What is your name? ')
#     greeting = f'Hello {name}'
#     if name.endswith('!'):
#         return greeting.upper()
#     return greeting
# print(greeting_yell())

def multiply(num1,num2):
    return num1*num2

def square(num):
    return multiply(num,num)

def calculate(first,second,operator):
    match operator:
        case '+':  return first + second
        case '-':  return first - second
        case '*':  return first * second
        case '/':  return first / second
        case '//': return first // second
        case '%':  return first % second
        case '**': return first ** second

def floating_point_arithmetic():
    operators = ['+','-','*','/','//','%','**']
    def promptify(string):
        return(f'==> {string}')
    print(promptify('Enter the first number:'))
    float_1 = float(input())
    print(promptify('Enter the second number:'))
    float_2 = float(input())

    for operator in operators:
        print(promptify(f'{float_1} {operator} {float_2} = {calculate(float_1,float_2,operator)}'))

# floating_point_arithmetic()

def second_to_last(string:str):
    return string.split()[-2]

def xor(boolean_1,boolean_2):
    if boolean_1 and not boolean_2:
        return True
    if boolean_2 and not boolean_1:
        return True
    return False

def oddities(list:list):
    return list[0::2]

import random

def teddy_age(name="Teddy"):
    print(f'{name} is {random.randrange(20,101)} years old') 

import datetime
def retirement_calculator():
    age:int = int(input('What is your age? '))
    retirement_age = int(input('At what age would you like to retire? '))
    years_until_retirement = retirement_age-age
    curr_year = int(datetime.date.today().year)
    print(curr_year)
    print(f'Its {curr_year}, you will retire in {curr_year+years_until_retirement}. Only {years_until_retirement} years left to go')


# retirement_calculator()


def center_of(string:str):
    length = len(string)
    middle_char = length // 2
    if length % 2 == 0: 
        return string[middle_char-1:middle_char+1]
    else:
        return string[middle_char]
    
# print(center_of('I Love Python!!!') == "Py")    # True
# print(center_of('Launch School') == " ")        # True
# print(center_of('Launchschool') == "hs")        # True
# print(center_of('Launch') == "un")              # True
# print(center_of('Launch School is #1') == "h")  # True
# print(center_of('x') == "x")                    # True

def negative(int):
   return -abs(int)

def repeat(string,count):
    for _ in range(count):
        print(string)

repeat('Hello', 3)

def crunch(string):
    chars = []
    for char in string:
        if not chars or chars[-1] is not char:
            chars.append(char)
    return ''.join(chars)

print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch(''))



def print_in_box(message):
    horizontal_rule = f'+-{"-" * len(message)}-+'
    empty_line = f'| {" " * len(message)} |'

    print(horizontal_rule)
    print(empty_line)
    print(f'| {message} |')
    print(empty_line)
    print(horizontal_rule)

def stringy(length):
    string = ''
    for idx in range(length):
        if idx % 2 == 0:
            string += '1'
        else:
            string += '0'
    return string

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101") 

def triangle(stars):
    for star_count in range(1,stars+1):
        print(f'{' '*(stars-star_count)}{'*'*star_count}')

triangle(5)

def madlibs():
    noun = input('Enter a noun ')
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    adverb = input("Enter an adverb: ")
    print(f"Do you {verb} your {adjective} {noun} {adverb}? "
      "That's hilarious!")
    print(f"The {adjective} {noun} {verb}s {adverb} over the lazy dog.")
    print(f"The {noun} {adverb} {verb}s up to Joe's {adjective} turtle.")

def twice(int:int):
    def isDouble(int):
        stringified = str(int)
        length = len(stringified)
        if length % 2 == 1:
            return False
        middle = length // 2
        part1 = stringified[0:middle]
        part2 = stringified[middle:]
       # print(part1,part2)
        if(part1 != part2):
            return False
        return True
    
    if isDouble(int):
        return int
    return int * 2


# print(twice(37) == 74)                  # True
# print(twice(44) == 44)                  # True
# print(twice(334433) == 668866)          # True
# print(twice(444) == 888)                # True
# print(twice(107) == 214)                # True
# print(twice(103103) == 103103)          # True
# print(twice(3333) == 3333)              # True
# print(twice(7676) == 7676)    

def get_grade(grade1,grade2,grade3):
    average = (grade1 + grade2 + grade3) / 3
    if 90 <= average <= 100:
        return 'A'
    if 80 <= average < 90:
        return 'B'
    if 70 <= average < 80:
        return 'C'
    if 60 <= average < 70:
        return 'D'
    return 'F'

def clean_up(string):
    cleaned_string = ''
    for i in range(len(string)):
        if str.isalpha(string[i]):
           cleaned_string = cleaned_string+string[i]
           continue
        else:
            if i is not 0 and not str.isalpha(string[i-1]):
                continue
            cleaned_string = cleaned_string + ' '
    return cleaned_string
        

print(clean_up("---what's my +*& line?") == " what s my line ")
import math;

def century(year):
    def get_century_string():
        century = math.ceil(year/100)
        return str(century)
    century_string = get_century_string()
    last_number = century_string[-1]
    if last_number in ['0','1','4','5','6','7','8','9']:
        century_string += 'th'
    elif last_number is '3':
        century_string += 'rd'
    elif last_number is '2':
        century_string += 'nd'
    elif last_number is '1':
        century_string += 'st'
    return century_string

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052))          # True
print(century(1127))          # True
print(century(11201))