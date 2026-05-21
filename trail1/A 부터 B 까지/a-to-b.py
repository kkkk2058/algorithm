A,B= map(int,input().split())

while A < B+1:
    if A % 2 ==1:
        print(A, end=' ')
        A*=2
    else:
        print(A, end=' ')
        A+=3
    