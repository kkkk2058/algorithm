N = int(input())


for i in range(N):
    ps = input()
    stack = []
    is_vps = True

    for j in ps:
        if j == '(':
            stack.append(j)


        elif j == ')':
            if stack:
                stack.pop()

            else:
                is_vps = False
                break


    if stack:  # 스택에 남은 괄호가 있으면 VPS가 아님
        is_vps = False
        
    print('YES' if is_vps  else 'NO')


    # if stack != []:
    # if stack : 
    # 둘이 같은 뜻이므로 아래꺼를 써보자!

    # 변수를 초기화 하는 위치를 잘 생각하자!