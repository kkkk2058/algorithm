area = 1
while True:
    n = input().split()
    area = int(n[0]) * int( n[1])
    if n[-1] == 'C':
        print(area)
        break
    else:
        print(area)
