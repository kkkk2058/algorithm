n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

def modify():
    global arr

    for j in queries:
        list = []
        sum = 0
        for k in j:
            
            list.append(k)
            start = list[0]
            end = list[-1]
        list_se = arr[start-1:end]
        for s in list_se:
            sum +=s

        print(sum)

                # sum += arr[k]


modify()