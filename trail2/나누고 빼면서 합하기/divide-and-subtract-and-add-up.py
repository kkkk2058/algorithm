n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code her

def modify(n,m):
    sum =0
    while m >=1:
        sum += A[m-1]
        if m %2 ==0:
            m //=2
        else:
            m-=1
        
    print(sum)

modify(n,m)