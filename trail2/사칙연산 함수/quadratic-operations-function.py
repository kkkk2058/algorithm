a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here

def math(a,o,c):
    result = 0
    if o == "+":
        return a + c
    elif o == "-":
        return a-c
    elif o =="/":
        return a//c
    elif o =="*":
        return a*c
    else:
        return False

k =math(a,o,c)
if k  != False:
    print(f"{a} {o} {c} = {k:.0f}")
else:
    print(False)