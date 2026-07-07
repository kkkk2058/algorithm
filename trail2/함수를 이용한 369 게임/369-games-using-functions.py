a, b = map(int, input().split())

def main(a,b):
    cnt = 0
    for i in range(a,b+1):
        if i % 3 ==0 or three_six_nine(i):
            cnt += 1
    return cnt

def three_six_nine(n):
    cnt1 = 1
    a =n 
    while a >= 10:
        a = a//10
        cnt1+=1
    result = False
    for i in range(cnt1):
        if n%10 ==3 or n%10 ==6 or n%10 ==9:
            #print(n)
            result = True
        n = n//10
    return result

print(main(a,b))
# for i in range(a,b):
#     print(three_six_nine(i))
# print(three_six_nine(a+1))
# print(three_six_nine(a+2))
# print(three_six_nine(a+3))