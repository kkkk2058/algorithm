N = int(input())

sum = 0
avg = 0

for i in range(N):
    n =int(input())
    sum += n
avg = sum/N
print(f"{sum} {avg:.1f}")