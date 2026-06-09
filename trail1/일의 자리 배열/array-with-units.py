arr = list(map(int,input().split()))



for i in range(10):
    next = arr[i] + arr[i+1]
    if next >= 10:
        next = (next) % (10)
    arr.append(next)


for j in range(10):

    print(arr[j],end=" ") 