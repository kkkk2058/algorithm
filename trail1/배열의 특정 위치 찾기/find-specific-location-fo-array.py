arr = list(map(int, input().split()))

n = len(arr)

sum_even = 0

cnt = 0
sum_three = 0
avg_three = 0

for i in range(n):
    if i % 2 == 1:
        sum_even +=arr[i]

    if i % 3 == 2:
        sum_three += arr[i]
        cnt +=1
    if cnt !=0 :
        avg_three = sum_three/cnt

print(f"{sum_even} {avg_three:.1f}")