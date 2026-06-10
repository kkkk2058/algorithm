arr = [0]*4
arr_count = []


for i in range(3):
    s, t = input().split()

    if s == "Y" and t >= "37":
        arr[0] +=1
    elif s == "N" and t >= "37":
        arr[1] +=1
    elif s == "Y" and t < "37":
        arr[2] +=1
    else:
        arr[3] +=1

if arr[0] >=2:
    arr.append("E")


# print(arr)
for i in arr:
    print(i,end=" ")