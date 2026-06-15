n = int(input())
a = list(map(int, input().split()))

minimize = a[0]
cnt = 0
for k in a:
    if minimize > k:
        minimize = k
        
for i in a:
    if i ==minimize:
        cnt+=1
print(minimize, cnt)