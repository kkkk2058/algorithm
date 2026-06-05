n = int(input())

cnt = 1
for i in range(n):
    for j in range(n):
        cnt %= 10
        if cnt == 0:
            cnt+=1
            print(cnt,end="")
            cnt+=1
        else:
            print(cnt,end="")
            cnt+=1
    print()