import numpy.linalg as np

n = int(input())
A = [[int (j) for j in input().split()] for i in range (n)]

d = int (np.det (A))

print(d)

