arr =list(map(int,input().split()))

min_list = []
max_list = []
mids = 500
mins = 500
maxs = 500


for i in arr:
    if i< mids:
        min_list.append(i)
    else:
        max_list.append(i)

maxs = max(min_list)
mins = min(max_list)

print(maxs, mins)
