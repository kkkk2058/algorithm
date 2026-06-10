n = int(input())

cnt = 0

# arr = []

# arr.append(n)

# for i in range(1,10):
#     a = arr[i-1] + arr[0]
#     arr.append(a)

# for elem in arr:
#     if elem %5 ==0:
#         cnt+=1
#     if cnt>=2:
#         break


for i in range(1,100):
    if cnt < 2:
        print(i * n, end =" " )
        if i * n %5 ==0:
            cnt+=1