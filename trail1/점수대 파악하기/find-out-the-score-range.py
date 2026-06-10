arr = list(map(int,input().split()))

arr_count = [0] * 11

for score in arr:
    score_10_num = score // 10
    score_10 = score_10_num * 10
    arr_count[score_10_num] += 1
    if score == 0:
        break
# print(arr_count)
for i in range(10,0,-1):
    print(f"{i * 10} - {arr_count[i]}")