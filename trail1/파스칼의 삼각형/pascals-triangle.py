n = int(input())

cnt = 1

elem = 1

arr = [[0 for i in range(n)]for j in range(n)]
for i in range(n):
    for j in range(n):

        if i == j:
            arr[i][j] = 1

        if i < j:
            arr[i][j] = 0
for i in range(n):
    arr[i][0] =1


for i in range(2,n):
    for j in range(1,n):
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
        
# for k in range(n):
#     cnt+=1
#     for i in range(1,cnt):
#         arr.append(1)





for i in range(n):
    for j in range(i+1):
        print( arr[i][j] , end=" ")
    print()