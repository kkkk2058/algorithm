n = int(input())

cnt = 0

list = []


for i in range(1,100):
    if cnt < 2:
        print(i * n, end =" " )
        if i * n %5 ==0:
            cnt+=1