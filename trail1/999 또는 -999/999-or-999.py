


min = 999
max = -999

n = list(map(int,input().split()))

list = []

for j in range(len(n)):
    
    if n[j] == 999 or n[j] == -999:
        break
    list.append(n[j])

# print(list)

for i in list:
    if i < min:
        min = i
    if i > max:
        max = i
    
print(max,min)
