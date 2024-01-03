# Initialize the matrix
row_1 = ['😅', '😅', '😅']
row_2 = ['😅', '😅', '😅']
row_3 = ['😅', '😅', '😅']

matrix = [row_1, row_2, row_3]

for row in matrix:
    print(row)


position = input("Enter the position (row and column): ")  # e.g., 11


row_pos = int(position[0]) - 1
col_pos = int(position[1]) - 1


matrix[row_pos][col_pos] = 'X'


for row in matrix:
    print(row)
