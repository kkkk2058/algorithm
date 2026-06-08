n = int(input())
arr = list(map(float, input().split()))

sum = 0
cnt = 0

for score in arr:
    sum += score
    cnt += 1

avg = sum/cnt

print(f"{avg:.1f}")

if avg >= 4.0:
    print("Perfect")
elif avg >=3.0:
    print("Good")
elif avg <= 3.0:
    print("Poor")