n = int(input())


for i in range(1,2*n+1,2):
    for _ in range(2*n-1 -i):
        print(" ",end="")
    for _ in range(i):
        print("*" , end= " ")
    print(" ")