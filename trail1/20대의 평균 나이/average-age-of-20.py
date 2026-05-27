cnt = 0
k=0

while True:
    n = int(input())
    if 20 <= n < 30:
        cnt += n
        k +=1
        # print(cnt)
    else:
        break
avg = cnt/k
print(f"{avg:.2f}")


    