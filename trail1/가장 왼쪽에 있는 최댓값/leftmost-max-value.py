import sys

n = int(input())
a = list(map(int, input().split()))
max_val = -sys.maxsize - 1 

for q in range(n):
    for idx, i in enumerate(a):
        # print(a)
        if max_val == a[0]:
            break
        if i == max(a):
            # max_val = max(a)
            print(idx+1,end=" ")
            a = a[:idx]
            break

