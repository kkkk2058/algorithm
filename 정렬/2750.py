n = int(input())

a= []

for i in range(n):
    i = int(input())
    a.append(i)        #for문 안에다 append를 넣어야됨

# [3,4,1,5,6,1]


for k in range(len(a) - 1):
    for s in range(len(a) - 1):  # 마지막 인덱스를 초과하지 않도록 범위를 조정
        if a[s] > a[s + 1]:     
            a[s], a[s + 1] = a[s + 1], a[s]  # 두 값을 교환

for m in a:
    print(m)