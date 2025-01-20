numbers=[]

N = int(input())

for i in str(N) :
    numbers.append(i)


numbers.sort(reverse=True)

print(int(''.join(map(str, numbers))))

