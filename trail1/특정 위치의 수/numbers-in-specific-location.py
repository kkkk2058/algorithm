arr = list(map(int,input().split()))

sum = 0
if len(arr) >= 10:
    sum += arr[2] + arr[4] + arr[9]

print(sum)