

# 입력 받기
N = int(input())  # 수의 개수 N
count = [0] * 10001


for i in range(N):
    number = int(input())
    count[number] += 1

for m in range(1, 10001):
    for n in range(count[m]):
        print(m)

