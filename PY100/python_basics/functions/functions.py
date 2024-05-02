def multiply(num1,num2):
    return num1 * num2

def bruce_eckel_quote():
    print('Python is executable pseudocode.')

def city(author,quote):
    print(f'{author} said: "{quote}"')

def squared_num(num):
    return num ** 2

def compare_by_length(str1,str2):
    if len(str1) < len(str2):
        return -1
    elif len(str1) > len(str2):
        return 1
    return 0

def transformation(string,replace):
   return str.replace(string,replace)

def greet(language_code):
    match language_code:
        case 'en':
            return 'Hi!'
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return 'Haai!'

def extract_language(locale):
    return locale[0:2]


def extract_region(locale):
    return locale.split('.')[0].split('_')[1]

def local_greet(locale):
    language = extract_language(locale)
    region = extract_region(locale)

    match (language, region):
        case ('en', 'US'):
            return 'Hey!'
        case ('en', 'GB'):
            return 'Hello!'
        case ('en', 'AU'):
            return 'Howdy!'
        case _:
            return greet(language)

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))  

print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!