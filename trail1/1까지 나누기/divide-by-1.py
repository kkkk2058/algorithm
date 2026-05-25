N =int(input())
cnt = 1

for i in range(1,N+1):
    N = N // i
    
    if N <= 1:
        break
print(i)