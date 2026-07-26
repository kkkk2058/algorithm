n = int(input())


def re(n):
    if n == 1:
        return 2
    if n == 2:
        return 4


    return (re(n-1) * re(n-2))%100

print(re(n))


# 2 4 8 32 56
