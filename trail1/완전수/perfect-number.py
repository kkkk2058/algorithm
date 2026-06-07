start, end = map(int, input().split())
cnt = 0
for i in range(start,end+1):
    
    sum = i
    for j in range(1,i):
        
        if i % j == 0:
            sum -= j

    if sum == 0:
        cnt+=1

    
print(cnt)