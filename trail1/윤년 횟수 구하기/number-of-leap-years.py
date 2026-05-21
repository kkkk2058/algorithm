# 4로 나누어 떨어지면 윤년
# 100으로 나누어떨어지고 #400으로 나누어떨어지지않으면 평년(즉 윤년이다)

N = int(input())
cnt = 0

for i in range(1, N+1):
    if i % 400 == 0:
        cnt += 1
    elif i % 100 == 0:
        continue
    elif i % 4==0:
        cnt += 1

print(cnt)