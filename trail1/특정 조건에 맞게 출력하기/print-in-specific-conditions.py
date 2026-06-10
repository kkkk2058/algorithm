arr = list(map(int,input().split()))



for k in arr:
    if k ==0:
        break
    if k % 2==0:
        print(k//2,end=" ")
    else:
        print(k+3,end=" ")
