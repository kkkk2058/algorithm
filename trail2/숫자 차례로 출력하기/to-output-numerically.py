n =int(input())

def re(a):
    if a ==0:
        return
    re(a-1)
    print(a,end=" ")
def re2(k):
    if k == 0:
        return
    re2(k-1)
    print(n-k+1,end=" ")

re(n)
print()
re2(n)