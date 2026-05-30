A,B = map(int,input().split(" "))

k = False

for i in range(A,B+1):
    if 1920 % i == 0 and 2880 % 2==0:
        k = True
        break
    else:
        continue

if k == True:
    print(1)
else:
    print(0)