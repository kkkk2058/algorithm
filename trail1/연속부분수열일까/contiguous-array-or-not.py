n1,n2 = map(int,input().split())


a = list(map(int,input().split()))
b = list(map(int,input().split()))



for i in range(n1):
    success = False
    if a[i] == b[0]:
        #print(b[0:],a[i:i+n2]) 
        if b[0:n2] == a[i:i+n2]:
            success = True
            break
        else:
            success = False



    
# print(success)
    

if success == True:
    print('Yes')
else:
    print('No')

