arr = list(map(int,input().split()))


sum = 0
cnt = 0

for num in arr:
    if num == 0:
        break
    if num % 2 ==0:
        sum += num
        cnt +=1

print(cnt,sum)