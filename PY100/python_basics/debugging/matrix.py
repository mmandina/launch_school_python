sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(sub_list[:])

matrix[0][0] = "X"
print(matrix) # [['X', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]