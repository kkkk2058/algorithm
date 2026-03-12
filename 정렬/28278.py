import sys

# 입력을 빠르게 받기 위한 설정
input = sys.stdin.readline

stack = []

N = int(input())
# N 은 int이므로 for문에 iterate로 넣을 수 없음 range 처리 해주어야 함
for i in range(N):
    command = input().split()
    # print(command)
    # input().split() 을 하게되면 문자열로 취급되기 때문에 
    # if 문 비교할때 문자열의 형태로 나타내주어야함
    if command[0] == "1" :
        stack.append(command[1])
    elif command[0] == "2":
        if stack != []:
            print(stack.pop(-1))
        else: print("-1")
    elif command[0] == "3":
        print(len(stack))
    elif command[0] == "4":
        if stack != []:
            print("0")
        else:
            print("1")
    elif command[0] =="5":
        if stack != []:
            print(stack[-1])
        else:
            print("-1")
