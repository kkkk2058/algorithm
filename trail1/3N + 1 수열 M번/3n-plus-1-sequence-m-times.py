n = int(input())


for i in range(n):
    cnt = 0
    k = int(input())
    while k != 1:
        if k % 2 == 0:
            k /= 2
            cnt+=1
        else:
            k = (k *3 + 1)
            cnt+=1
    print(cnt)