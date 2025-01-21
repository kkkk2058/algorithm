N, M  = map(int, input().split())

cards = list(map(int, input().split()))

max_num = 0


for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            current_num = cards[i] +cards[j] +cards[k]
            if current_num <= M and current_num > max_num:
                max_num = current_num

print(max_num)


