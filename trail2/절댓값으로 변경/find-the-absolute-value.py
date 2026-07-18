n = int(input())
arr = list(map(int, input().split()))

def modify(arr):
    for i in range(n):
        if arr[i] < 0:
            arr[i] *=-1
        print(arr[i],end=" ")

modify(arr)