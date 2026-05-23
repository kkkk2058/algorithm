import sys
A, B = map(int,sys.stdin.readline().split())

prod = 1


for i in range(1,B+1):
    if i % A == 0:
        prod *= i

print(prod)