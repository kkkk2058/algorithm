n,q = map(int,input().split())

lists = list(map(int,input().split()))

# query = list(map(int,input().split()))


for i in range(q):
    query = list(map(int,input().split()))

    if query[0] == 1:
        print(lists[query[1]-1])

    elif query[0] == 2:
        if not query[1] in lists: 
            print(0)
            
        for k, j in enumerate(lists):
            if query[1] == j:
                print(k+1)
                break

    elif query[0] == 3 :
        list_3 = lists[query[1]-1:query[2]]

        for o in list_3:
            print(o ,end=" ")
        print()
    
