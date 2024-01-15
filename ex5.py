import numpy as np
n = int(input())
A = [[int(j) for j in input().split()]for i in range (n)]
n = int(input())
B = [[int(j) for j in input().split()]for i in range (n)]
A = np.linalg.inv (A)
C = A.dot(B)
print(C)