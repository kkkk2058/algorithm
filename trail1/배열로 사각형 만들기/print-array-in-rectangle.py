arr_2 = [[0 for i in range(5)] for i in range(5)]


for i in range(5):
    arr_2[0][i] = 1
    arr_2[i][0] = 1

for i in range(4):
    for j in range(4):
        arr_2[i+1][j+1] = arr_2[i+1][j] + arr_2[i][j+1]

for k in arr_2:
    for l in k:
        print(l,end=" ")
    print()
