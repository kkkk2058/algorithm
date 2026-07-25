a,b,c = list(map(int,input().split()))

# 재귀함수는 값을 저장해놓기 어렵다, 값을 더해야하는데 재귀로 부르니까

mul = a*b*c

def rec(mul):
    if mul <10:
        return mul

    num = mul % 10
    #print(mul,num)

    return rec(mul//10) + num
    

print(rec(mul))