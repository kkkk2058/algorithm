n = int(input())
price = list(map(int, input().split()))

cnt = 0

for j in range(n-1,0,-1):
    profit = price[j]
    for i in range(j-1,0,-1):
        if profit > price[i]:
            if cnt < profit - price[i]:
                cnt = profit - price[i]
        else:
            continue

print(cnt)