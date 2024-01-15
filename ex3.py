import numpy as np
n = int(input())
A = [[int(j) for j in input().split()] for i in range (n)]
d = np.linalg.matrix_power (A,-3)
print (d)
for i in d: 
    print (i)