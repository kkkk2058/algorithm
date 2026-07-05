n, m = map(int, input().split())

def lcm(n,m):
    for i in range(1,10000):
        if i % n == 0 and i % m == 0:
            print(i)
            break

lcm(n,m)

# def gcd(n,m):
#     while n