cnt = 0 
while True:
    n =int(input())
    if n % 2 ==1:
        continue
    else:
        k = n//2
        print(k)
        cnt +=1
        if cnt >= 3:
             break
#     print("1")
# print('2')