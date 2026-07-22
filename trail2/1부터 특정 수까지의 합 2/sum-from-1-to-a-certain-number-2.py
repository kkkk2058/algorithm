n= int(input())



def re(x):
    if x ==0:
        return 0
    return re(x-1) + x

print(re(n))