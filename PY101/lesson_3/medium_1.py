def flintstones_rock():
    for num_hyphens in range(1,11):
        print(f'{'-'*num_hyphens}The Flintstones Rock!')

flintstones_rock()


def factors(number):
    divisor = number
    result = []
    while divisor >=1:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

print(factors(20))