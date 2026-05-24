A = int(input())


for i in range(1,A+1):
    if i % 2 ==0 and i%4!=0:
        continue
    k = i//8
    if k%2 ==0:
        continue
    m = i % 7
    if m < 4:
        continue
    print(i, end=' ')