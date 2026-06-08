arr = list(map(float,input().split()))

sum = 0

for score in arr:
    sum += score

avg = sum/len(arr)

print(f"{avg:.1f}")