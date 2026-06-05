a,b = map(int,input().split())

for i in range(1,10):
    for j in range(0,b-a+1,2):
        print(f"{b-j} * {i} = {(b-j)*i}",end=" ")
        if j < b-a:
            print("/",end=" ")
    print()