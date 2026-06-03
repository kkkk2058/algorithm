N = int(input())

for i in range(2*N-1,0,-2):
    for k in range(0,2*N-1-i,2):
        print(" ", end =" ")
        # continue
    for j in range(i):
        print("*",end=" ")
    print(" ")
