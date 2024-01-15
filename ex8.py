import numpy as np
n = int(input())
A = [[int(j) for j in input().split()] for i in range (n)]
A = np.array (A)
l, h = np.linalg.eig(A)
m1 = abs(l[0])
m2 = abs(l[1])
k1 = 0
k2 = 1
if m2>m1:
    m1,m2 = m2,m1
    k1,k2 = k2,k1

for i in range (2, len(l)):
    if abs(l[i])>m2 and abs(l[i])<m1:
        m2 = abs(l[i])
        k2 = i
    elif abs(l[i])>m1:
        m2,m1 = m1,abs(l[i])
        k2,k1 = k1,i
for i in range (0,n):
    print (h[k2][i])