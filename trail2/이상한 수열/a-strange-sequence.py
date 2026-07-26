n = int(input())


def re(n):
    if n == 1:
        return 1

    if n == 2:
        return 2

    return re(n-1) + re(n//3) 

print(re(n))