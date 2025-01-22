N = int(input())
stack= []

for _ in range(N):
    string = input()
    string += " "

    for i in string:
        if i != " ":
            stack.append(i)
        else:
            while stack:
                print(stack.pop(), end='')
            print(' ', end='')
            

        


        
