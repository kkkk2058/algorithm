arr_2d = [list(input().split()) for _ in range(5)]


for j in range(5):
    for i in arr_2d[j]:
        print(i.upper(),end=" ")
    print()