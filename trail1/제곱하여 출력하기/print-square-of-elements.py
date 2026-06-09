n = int(input())



arr = list(map(int,input().split()))



x = [i**2 for i in arr]

[print(k,end=" ") for k in x]
