n = int(input())

hum = 0

for human in range(n):
    arr = list(map(int,input().split()))
    sum = 0
    cnt = 0
    for score in arr:
        sum +=score
        cnt +=1
    avg = sum/cnt
    # print(avg)
    if avg >= 60:
        print("pass")
        hum +=1
    else:
        print("fail")

print(hum)