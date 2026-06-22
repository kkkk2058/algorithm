
n =4
arr_2d = [ list(map(int,input().split())) for _ in range(n)]

for j in range(n):
    sum = 0
    for i in arr_2d[j]:
        sum += i
    print(sum)