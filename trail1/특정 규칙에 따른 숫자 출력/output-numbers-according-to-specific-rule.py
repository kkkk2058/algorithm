n = int(input())
cnt = 1
for i in range(n,0,-1):
    for j in range(n,0,-1):
        if i<j:
            print(" ",end= " ")
        else:
            if cnt ==10:
                cnt =1
            print(cnt,end=" ")
            cnt+=1
    print()