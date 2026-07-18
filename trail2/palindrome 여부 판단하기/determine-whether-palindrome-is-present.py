A = input()

def modify(string):
    reverse_string = string[::-1]
    # print(reverse_string)
    if string == reverse_string:
        print("Yes")
    else:
        print("No")

modify(A)

