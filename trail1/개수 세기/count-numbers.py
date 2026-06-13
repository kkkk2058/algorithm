n,m = map(int,input().split())


list = list(map(int,input().split()))
cnt = 0


for i in list:
    if m == i:
        cnt+=1

print(cnt)


