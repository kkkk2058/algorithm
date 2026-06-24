arr_1 = []
for _ in range(3):
    arr_1.append(list(map(int, input().split())))

input()
arr_2 = []
for _ in range(3):
    arr_2.append(list(map(int, input().split())))

for i in range(3):
    for j in range(3):
        print(arr_1[i][j] * arr_2[i][j], end=" ")
    print()
