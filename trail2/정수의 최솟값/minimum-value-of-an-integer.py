a, b, c = map(int, input().split())

def min(a,b,c):
    min = 0
    if a <= b and a <= c:
        min = a
    elif b <= a and b <=c:
        min = b
    elif c <= a and c <= b:
        min = c

    return min

print(min(a,b,c))