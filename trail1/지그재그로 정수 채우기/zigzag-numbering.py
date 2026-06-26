n, m = map(int, input().split())

num = 0
# Please write your code here.
arr_2 = [[0 for _ in range(m)] for _ in range(n)]

for i in range(m):
    if i % 2 == 0:
        for j in range(n):
            arr_2[j][i] +=num
            num +=1
    else:
        for j in range(n-1,-1,-1):
            arr_2[j][i] +=num
            num+=1


for k in arr_2:
    for h in k:
        print(h, end =" ")
    print()