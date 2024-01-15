import numpy.linalg as np
n = int(input())
A = [[int(j) for j in input().split()]for i in range (n)]
l, h = np.eig (A)
sum = 0
for i in range (0, len(l)):
    sum += l[i]
print(int(sum))