'''
Input: year (int)
Output: return a boolean, true if leap year, false if not
Rules: If the year is divisible by 400, it is a leap year.
If the year is divisible by 100 but not by 400, it is not a leap year.
If the year is divisible by 4 but not by 100, it is a leap year.
All other years are not leap years.

Mental model of the problem (optional) if div by 400, true. if div by 4 but not 100, return true. else return false
Examples/Test Case:
Data Structures:
Algorithm: for odd in range 1 - 100, increment by 2
Code with Intent:

'''

def is_leap_year(year):
    if year >=1752:
        if year % 400 == 0:
            return True
        if year % 4 == 0 and year % 100 != 0:
            return True
    else:
        if year % 4 == 0:
            return True
    return False

print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == True)
print(is_leap_year(1100) == True)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == True)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)