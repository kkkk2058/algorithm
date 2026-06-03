n = int(input())


for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*",end=" ")

        else:
            if j < i:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()


# i= 2, j = 0 ,1 까지는 *이므로 * * k k k * 에서  * * 까지는 출력 이후에는 K이다.