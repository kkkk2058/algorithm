n = int(input())

cnt = 1

for i in range(1,n+1):
    for j in range(1,n+1):
        if i % 2 ==0:
            print(cnt+(i-1)*n-1,end=" ")
            cnt -= 1
        else:
            print(cnt+(i-1)*n,end=" ")
            cnt += 1
    print()