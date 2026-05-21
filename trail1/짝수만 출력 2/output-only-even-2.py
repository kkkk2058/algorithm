B, A = map(int,input().split())

i = 0
while i < B-A + 1:
    if i %2 ==0:
        print(B-i, end= ' ')
    i += 1