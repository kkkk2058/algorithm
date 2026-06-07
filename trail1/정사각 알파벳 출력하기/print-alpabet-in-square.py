n = int(input())
cnt =65
for i in range(1,n+1):
    for j in range(1,n+1):
        if j == n:
            print(chr(cnt),end="")
            print()
            cnt+=1
        else:
            print(chr(cnt),end="")
            cnt+=1