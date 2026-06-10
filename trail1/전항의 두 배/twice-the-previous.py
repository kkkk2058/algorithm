a0,a1 = map(int,input().split())


arr = [a0,a1]

for i in range(10):
    arr.append(arr[i+1]+arr[i]*2)
    print(arr[i],end=" ")

# 0 1 2 3 4 5 6 7 8 9
# 3 4 5
# # for i in range(8)