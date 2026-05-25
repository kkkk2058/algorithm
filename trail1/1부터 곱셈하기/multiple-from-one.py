N = int(input())

cnt = 1

for i in range(1,11):
    cnt *= i
    if N <= cnt:
        print(i)
        break