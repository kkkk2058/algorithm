n = int(input())

def reculsive(k,cnt):
    if k == 1:
        return cnt
    if k %2 ==0:
        k //=2
    else:
        k = k//3
    cnt +=1
    return reculsive(k,cnt)

print(reculsive(n,0))