n = int(input())

arr_2 = [[0 for i in range(n)] for j in range(n)]

num = 1

for j in range(n-1,-1,-1):
    if n % 2 == 0:
        if j % 2 == 1:
            for i in range(n-1,-1,-1):
                arr_2[i][j] +=num
                num +=1
        else:
            for i in range(n):
                arr_2[i][j] +=num
                num +=1
    else:
        if j % 2 == 0:
            for i in range(n-1,-1,-1):
                arr_2[i][j] +=num
                num +=1
        else:
            for i in range(n):
                arr_2[i][j] +=num
                num +=1


for num in range(n):
    for num1 in range(n):
        print(arr_2[num][num1], end=" ")
    print()