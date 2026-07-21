n = int(input())

# Please write your code here.

def re(a):

    if a==0:
        return
    
    print(a,end=" ")
    re(a-1)
    print(a,end=" ")

re(n)