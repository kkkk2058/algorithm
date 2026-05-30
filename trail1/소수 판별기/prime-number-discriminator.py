N = int(input())

decimal = True

for i in range(2,N):
    if N % i == 0:
        decimal = False
        break
if decimal == True:
    print("P")
else:
    print("C")

