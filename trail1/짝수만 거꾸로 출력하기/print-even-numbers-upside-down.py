n = int(input())


arr = list(map(int,input().split()))

k = []
arr = arr[::-1]
for i in arr:
    if i % 2 ==0:
        print(i,end=" ")
# print(k)       
# for j in k:
#     print(k[j],end=" ")