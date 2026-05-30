N = int(input())

k = False

for i in range(2,N):
    if N % i == 0:
        k = True
    else:
        continue

if k == True:
    print('C')
else:
    print('N')