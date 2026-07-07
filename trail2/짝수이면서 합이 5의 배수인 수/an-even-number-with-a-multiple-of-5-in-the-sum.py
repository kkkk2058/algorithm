n = int(input())

def get_five_even(n):
    a = n //10
    b = n % 10
    if n % 2==0 and (a+b) %5==0:
        result= "Yes"
    else:
        result= "No"
    return result

print(get_five_even(n))

# def get_five_even(n):
#     a = n/10
#     b = n% 10
#     print(a,b)

# print(get_five_even(n))