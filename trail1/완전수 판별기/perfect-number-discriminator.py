N = int(input())

cnt = N
for i in range(1, N):
    if N % i == 0:
        cnt -= i

# print(cnt)
if cnt == 0:
    print("P")
else:
    print("N")