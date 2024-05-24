numbers = [1, 2, 3, 4, 5]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}
title = "Flintstone Family Members"
statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}

print(numbers[::-1])
print(list(reversed(numbers)))

numbers_2 = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

print(95 in numbers_2)

print(42 in range(10,101))
print(100 in range(10,101))
print(101 in range(10,101))

print(numbers.pop(2))
print(numbers)

print(isinstance(numbers,list))
print(isinstance(table,list))

print(title.center(40,' '))

print(statement1.count('t'))
print('Spot' in ages)

additional_ages = {'Marilyn': 22, 'Spot': 237}
ages.update(additional_ages)