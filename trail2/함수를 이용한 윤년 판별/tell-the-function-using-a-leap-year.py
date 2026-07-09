y = int(input())

# Please write your code here.

def yun(y):
    if y % 4 ==0:
        if y % 100 ==0 and y % 400 != 0:
            return True
        return False
    return True

if yun(y) == False:
    print("true")
else:
    print("false")
