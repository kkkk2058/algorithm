n = int(input())

for i in range(1,n+1):
    if i % 2 == 0:
        for j in range(2*n-i,-1,-2):
            print("*",end=" ")
    else:
        for j in range(1,i+1,2):
            print("*",end=" ")
        
    print()

for i in range(n,0,-1):
    if i % 2 == 0:
        for j in range(2*n-i,-1,-2):
            print("*",end=" ")
    else:
        for j in range(1,i+1,2):
            print("*",end=" ")
        
    print()