def solution(s):
    answer = True
    stack = []

    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if not stack:
                return False
              #  true false 조건을 잘 생각해보자
            stack.pop()
    
    return len(stack) == 0
