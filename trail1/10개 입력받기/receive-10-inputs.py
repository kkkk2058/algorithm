arr = list(map(int,input().split()))
sum = 0
cnt = 0

for i in range(len(arr)):
    if arr[i] == 0:
        break
    sum += arr[i]
    cnt +=1



avg = sum/cnt

print(f"{sum} {avg:.1f}")