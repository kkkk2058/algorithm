A,B=map(int,input().split())
total= ""
k = A//B # 4
mod = A%B # 2

for i in range(20):

    next = mod*10 #20

    k_1 = next//B # 6
    mod = next%B # 2

    # print(k_1, end='')
    total += str(k_1)

print(f"{k}.{total}")