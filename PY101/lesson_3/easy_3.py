numbers = [1, 2, 3, 4]
numbers.clear()
while numbers:
    numbers.pop()

print([1, 2, 3] + [4, 5])


def is_color_valid(color):
    return color == "blue" or color == "green"

