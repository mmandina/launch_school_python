'''
Input: two strings of different length, float length both in meters
Output: one string, the short string + long string + short string
Rules: strings must be diff length
Mental model of the problem (optional): find the shortest of the two strings, set it to short, other to long. concat, and return
Code with Intent:
'''

def short_long_short(str1,str2):
    if len(str1)<len(str2):
        short = str1
        long = str2
    else:
        short = str2
        long = str1
    return short + long + short

print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")