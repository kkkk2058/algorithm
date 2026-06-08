arr = list(map(int,input().split()))
sum_odd = 0
sum_even = 0
sum = 0
sum_2 = 0
for i in range(len(arr)):
    if i % 2 ==0:
        sum = [arr[i] for i in range(0,len(arr),2)]
    else:
        sum_2 = [arr[i] for i in range(1,len(arr)+1,2)]

for i in sum:
    sum_odd +=i

for i in sum_2:
    sum_even +=i



if sum_odd > sum_even:
    print(sum_odd-sum_even)
else:
    print(sum_even-sum_odd)