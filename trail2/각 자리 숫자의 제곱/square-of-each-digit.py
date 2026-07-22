n= int(input())

# Please write your code here.

def digit(n):
    if n < 10:
        return n**2
    a = n
    a //=10
    b = n
    b %=10
    
    return digit(a) + b**2
    
print(digit(n))