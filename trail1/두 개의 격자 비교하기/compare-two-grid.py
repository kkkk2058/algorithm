n,m = map(int,input().split())

arr_1 = []

for i in range(n):
    arr_1.append(list(map(int,input().split())))


arr_2 = []

for i in range(n):
    arr_2.append(list(map(int,input().split())))


arr = [[1 for i in range(m)] for j in range(n)]

for i in range(n):
    for j in range(m):
        if arr_1[i][j] == arr_2[i][j]:
            arr[i][j] = 0

for i in range(n):
    for j in range(m):
        print(arr[i][j],end=" ")
    print()
