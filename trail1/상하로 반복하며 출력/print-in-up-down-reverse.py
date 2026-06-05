n = int(input())


# for j in range(1,n+1):
#     print(f"{j}{n+1-j}{j}{n+1-j}{j}")


for j in range(1,n+1):
    for k in range(n):
        if k % 2 ==0:
            print(f"{j}",end="")
        else:
            print(f"{n+1-j}",end="")
        # print(f"{j}{n+1-j}{j}{n+1-j}{j}")
    print()
