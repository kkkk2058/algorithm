n = int(input())

def re(n):
    if n == 0 :
        return 0
    if n == 1:
        return 1
    if n % 2 == 1:
        return re(n-2) + n
    else:
        return re(n-2) + n


print(re(n))