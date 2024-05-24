famous_words = "seven years ago..."

def append_four_one():
    return 'Four score and '+ famous_words

def append_four_two():
    return f'Four score and {famous_words}'

print(append_four_one())

munsters_description = "the Munsters are CREEPY and Spooky."

print(munsters_description.capitalize())

print(munsters_description.swapcase())

str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

print('Dino' in str1)
print('Dino' in str2)

flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]

flintstones.extend(['Dino','Happy'])

advice = "Few things in life are as important as house training your pet dinosaur."

print(advice[0:advice.index('house')])
print(advice.split("house")[0])

advice = "Few things in life are as important as house training your pet dinosaur."

advice.replace('important','urgent')





