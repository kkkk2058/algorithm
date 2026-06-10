a, b = map(int,input().split())

arr = []

arr_count = [0] * b
for i in range(11):
    if a <=1:
        break
    q = a // b
    mod = a % b

    a = q
    arr.append(mod)

for j in arr:
    arr_count[j] += 1

sum = 0

for k in arr_count:
    sum += k*k
    # print(k,sum)

print(sum)