a, b = map(int, input().split())

# Please write your code here.

def on(a,b):
    cnt  = 0
    is_true = True

    for i in range(a,b+1):
        is_true = True
        if i %2  ==0:
            is_true = False
        k = i % 10
        if k ==5:
            is_true =False
        if i %3  ==0 and i%9  !=0:
            is_true = False

        if is_true == True:
            cnt +=1
            
    return cnt


print(on(a,b))