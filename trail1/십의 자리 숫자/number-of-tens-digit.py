arr = list(map(int,input().split()))

arr_count = [0] * 10

for i in arr:
    i_10 = i % 100
    i_10 = i_10 // 10
    arr_count[i_10] +=1
    if i ==0:
        break

for k in range(1,10):

    print(f"{k} - {arr_count[k]}")