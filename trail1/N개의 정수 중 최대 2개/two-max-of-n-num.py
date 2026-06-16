import sys
n = int(input())
a = list(map(int, input().split()))

list = []
max = -sys.maxsize - 1
for i in range(2):
    max = -sys.maxsize - 1
    for j in a:

        if max < j:
            max = j
    # print(list)
    # print(a)
    
    list.append(max)
    a.remove(max)

for k in list:
    print(k,end=" ")


