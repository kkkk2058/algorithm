
n = list(map(int, input().split()))

sum = 0
avg = 0
cnt = 0
for i in n:
    if i < 250:
        sum += i                   
        cnt+=1
    else:
        break

avg = sum / cnt
print(f"{sum} {avg:.1f}")
