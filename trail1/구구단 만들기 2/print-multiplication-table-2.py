a,b =map(int,input().split())
for i in range(1,5):
    for j in range(b,a-1,-1):
        print(f"{j} * {2*i} = {j*2*i}",end=" ")
        if j > a:
            print("/",end=" ")
    print()