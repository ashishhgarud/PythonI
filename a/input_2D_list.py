# How to input matrix (or 2D list) in Python?
# where n is no of elements in columns while m is no of elements in a row.
#
# In pythonic way, this will create a list of list

# in a one-liner by using list comprehension:
matrix = [[0 for j in range(n)] for i in range(m)]

#
matrix = [x[:] for x in [[0]*n]*m]

#
arr2d = [[j for j in input().strip()] for i in range(n)]

# initialize your matrix in a nested loop
matrix = []
for i in range(0,m):
    matrix.append([])
    for j in range(0,n):
        matrix[i].append(0)

# for numbers
n = int(input().strip())
m = int(input().strip())
a = [[0]*n for _ in range(m)]
for i in range(n):
    a[i] = [int(j) for j in input().strip().split(" ")]
print(a)

# for characters
n = int(input().strip())
m = int(input().strip())
a = [[0]*n for _ in range(m)]
for i in range(n):
    a[i] = list(input().strip())
print(a)

# or
n = int(input().strip())
n = int(input().strip())
a = []
for i in range(n):
    a[i].append(list(input().strip()))
print(a)

