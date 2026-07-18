n = int(input())
arr = list(map(int, input().split()))

def two(arr):
    for i in range(n):
        if arr[i] %2 == 0:
            arr[i] //= 2

    return arr
    
two(arr)
for j in arr:
    print(j,end=" ")
# print(two(arr))