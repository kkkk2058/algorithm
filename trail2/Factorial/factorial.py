n = int(input())

def re(n):
    if n == 0:
        return 1
    if n == 1:
        return 1

    return re(n-1) * n

print(re(n))