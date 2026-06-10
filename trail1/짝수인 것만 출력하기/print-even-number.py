n = int(input())

arr = list(map(int,input().split()))

[print(i,end=" ") for i in arr if i% 2 == 0]