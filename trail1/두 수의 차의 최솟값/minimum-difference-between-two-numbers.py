import sys

n = int(input())
arr = list(map(int,input().split()))


abs = sys.maxsize

for i in range(n):
    for j in arr[i+1:]:
        if abs > j-arr[i]:
            abs = j-arr[i]
            # print(j,arr[i])
print(abs)