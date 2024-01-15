import numpy as np
n = int(input())
A = [[int(j) for j in input().split()]for i in range (n)]
l, h = np.linalg.eig(A)
m = 0
for i in range (0, len(l)):
    if abs(l[i])>m:
        m = abs(l[i])
print (m)