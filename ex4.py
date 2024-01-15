import numpy as np
n = int (input())
A = [[int(j) for j in input().split()] for i in range (n)]
A = np.array(A)
n = int(input())
B1 = [[int(j) for j in input().split()]for i in range (n)]
B1 = np.array(B1)
B2 = np.linalg.inv (B1)
Anew = (B2.dot(A)).dot(B1)
print (Anew)

