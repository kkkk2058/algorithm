n = int(input())

arr= []

arr.append(1)
arr.append(n)
arr.append(n+1)



for i in range(2,100):
    
    if arr[i] > 100:
        # for num in range(i):
        #     print(arr[num],end=" ")
        break
    arr.append(arr[i-1] + arr[i])

for num in arr:
    print(num,end=" ")