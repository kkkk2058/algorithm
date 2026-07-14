a, b = map(int, input().split())

# Please write your code here.

def so(n):
    for j in range(2,n):
        if n % j ==0:
            return False
    return True 


def ja(n):
    sum = 0
    if n < 9:
        sum = n
    elif 10 < n < 99:
        k = n // 10
        l = n % 10
        sum = k + l
    else:
        sum = 1
    return sum

def main(a,b):
    cnt = 0
    for i in range(a,b+1):
        
        if so(i) and ja(i) % 2 == 0:
            cnt += 1
    return cnt




print(main(a,b))


