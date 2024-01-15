import numpy as np
n = int(input())
A = [[int(j) for j in input().split()] for i in range (n)]
d = np.trace (A)
print (d)