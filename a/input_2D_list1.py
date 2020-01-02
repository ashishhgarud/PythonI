# A basic code for matrix input from user

R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

# Initialize matrix
matrix = []
print("Enter the entries rowwise:")

# For user input
for i in range(R):  # A for loop for row entries
    a = []
    for j in range(C):  # A for loop for column entries
        a.append(int(input()))
    matrix.append(a)

# For printing the matrix
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end=" ")
    print()

####
# one-liner logic to take input for rows and columns
mat = [[int(input()) for x in range(C)] for y in range(R)]

# Code #2: Using map() function and Numpy.
####
import numpy as np

R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

print("Enter the entries in a single line (separated by space): ")

# User input of entries in a
# single line separated by space
entries = list(map(int, input().split()))

# For printing the matrix
matrix = np.array(entries).reshape(R, C)
print(matrix)
