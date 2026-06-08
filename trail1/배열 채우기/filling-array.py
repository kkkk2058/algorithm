arr = list(map(int,input().split()))

cnt = 0 
for num in range(10):
    if arr[num] == 0:
        break
    cnt +=1

# print(arr[:cnt-1])
# print(cnt)

for i in range(cnt-1,-1,-1):
    print(arr[i],end=" ")