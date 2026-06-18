n = int(input())
nums = list(map(int, input().split()))

list = []

result = []


for i in nums:

    if i not in list:
        if i not in result:
            list.append(i)
            result.append(i)
        else:
            continue
    else:
        list.remove(i)

# for j in list:

if list:
    max = list[0]

for k in list:
    if max < k:
        max = k
if list:
    print(max)
else:
    print("-1")
