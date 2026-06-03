n = int(input())


# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i % 2==0:
#             for _ in range(n//3,-1,-1):
#                 print("*", end="  ")
#         else:
#             for _ in range(n):
#                 print("*", end="  ")

#         print()



# for j in range(1,n+1):
#     if j % 2==0:
#         for _ in range(j):
#             print(" ",end=" ")
#         for _ in range((n-j+1)//2):
#             print("*", end=" ")
#     else:
#         for _ in range(2*(j-1)):
#             print(" ", end=" ")

#         for _ in range(n-2*(j-1)):
#             print("*", end=" ")

#     print()


for i in range(n):
    for j in range(n):
        if j % 2 == 0:
            if i > 0:
                print(" ",end=" ")
            else:
                print("*",end=" ")
        else:
            # if i % 2 ==1:
            #     print("d",end=" ")
            # else:
            #     # if 
            
            if j<i:
                print(" ",end=" ")
            else:
                print("*",end=" ")


    print()