
n = int(input())
arr = list(map(int, input().split()))

def find_max(idx):
    if idx == n-1:
        return arr[idx]

    max = find_max(idx+1)

    if max > arr[idx]:
       return max
    else:
        return arr[idx]
    


print(find_max(0))
