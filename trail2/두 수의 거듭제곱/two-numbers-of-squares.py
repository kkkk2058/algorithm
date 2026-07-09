a, b = map(int, input().split())

# Please write your code here.\

def ex(a,b):
    result = 1
    for i in range(b):
        result *= a
    return result

print(ex(a,b))