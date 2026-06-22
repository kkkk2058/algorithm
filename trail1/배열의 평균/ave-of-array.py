arr_2d = [list(map(int,input().split())) for _ in range(2)]

sum = 0
for i in range(2):
    sum = 0
    for j in range(4):
        sum += arr_2d[i][j]
    print(sum/4,end=" ")

print()
for i in range(4):
    sum = 0
    for j in range(2):
        sum += arr_2d[j][i]
    print(sum/2,end=" ")
print()

sum = 0
for i in range(2):
    for j in range(4):
        sum += arr_2d[i][j]
print(f"{sum/8:.1f}",end=" ")
