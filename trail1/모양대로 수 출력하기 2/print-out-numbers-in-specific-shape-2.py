n = int(input())

cnt = 2

for i in range(2,n+2):
    for j in range(2,n+2):
        if cnt == 10:
            cnt = 2
        print(cnt,end=" ")
        cnt +=2
    print()