multiple_3 = True
for i in range(5):
    n = int(input())

    if n % 3 !=0:
        multiple_3 = False
        break

if multiple_3 == True:
    print(1)
else:
    print(0)