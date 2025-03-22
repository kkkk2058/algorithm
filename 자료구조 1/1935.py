# 피연산자 개수 입력받기
stack = []
N = int(input().strip())  # 개수 입력

# 후위 표기식 입력받기
expression = input().strip()

# 피연산자에 해당하는 값 입력받기 (정수 변환)
values = {}
for i in range(N):
    values[chr(ord('A') + i)] = int(input().strip())  # 정수로 변환하여 저장

# 후위 표기식 계산
for ch in expression:
    if ch.isalpha():  # 피연산자 (A~Z)인 경우
        stack.append(values[ch])  # 스택에 push
    elif ch in "+-*/":  # 연산자일 경우
        b = stack.pop()  # 피연산자 꺼내기
        a = stack.pop()

        # 올바른 연산 수행
        if ch == '+':
            stack.append(a + b)
        elif ch == '-':
            stack.append(a - b)
        elif ch == '*':
            stack.append(a * b)
        elif ch == '/':
            stack.append(a / b)  # 부동소수점 연산

# 최종 결과 출력 (소수점 두 자리까지)
print(f"{stack[-1]:.2f}")
