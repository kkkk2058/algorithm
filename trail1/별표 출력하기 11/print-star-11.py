n = int(input())


# for j in range(2*n+1):
#     if j % 2==0:
#         print("*"*(2*n+1),end=" ")
#     else:
#         print("#"*(2*n+1),end=" ")
# print()


for i in range(2*n+1): 
    for j in range(2*n+1):
        if i % 2==0:
            print("*", end=" ")
        else:
            if j % 2 ==0:
                print("*", end=" ")
            else:
                print(" ", end= " ")
    print()
