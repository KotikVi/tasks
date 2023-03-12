#     2. Counting islands

# You have a matrix MxN that represents a map. There are 2 possible states on the map: 1 - islands, 0 - ocean. Your task is to calculate the number of islands in the most effective way. Please write code in Python 3.

# Inputs:
# M N
# Matrix

# Examples:
# Input:
# 3 3
# 0 1 0
# 0 0 0
# 0 1 1
# Output: 2

# Input:
# 3 4
# 0 0 0 1
# 0 0 1 0
# 0 1 0 0
# Output: 3

# Input:
# 3 4
# 0 0 0 1
# 0 0 1 1
# 0 1 0 1
# Output: 2

m = int(input("Enter the number of rows(m):"))
n = int(input("Enter the number of columns(n):"))

input_matrix = [[int(input()) for x in range (n)] for y in range(m)]

def check_neighbors(matrix, i, j, m ,n ):
    if m > i >= 0 and n > j >= 0:
        if matrix[i][j]:
            matrix[i][j]=0
        else:
            return
        check_neighbors(matrix, i-1, j, m, n)
        check_neighbors(matrix, i, j-1, m, n)
        check_neighbors(matrix, i+1, j, m, n)
        check_neighbors(matrix, i, j+1, m, n)

count = 0
for i in range(m):
    for j in range(n):
        if input_matrix[i][j]:
            count +=1
            check_neighbors(input_matrix, i, j, m, n)

print(count)