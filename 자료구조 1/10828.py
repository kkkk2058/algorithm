
# def main():
#     commands = sys.stdin.read().splitlines()
#     N = int(commands[0])
#     stack = []
#     result = []

#     for i in range(1, N+1):
#         if 
import sys


n = int(sys.stdin.readline())
stack = []

for i in range(n):
    input_line = sys.stdin.readline().split()
    command = input_line[0]


    if command == "push":
        stack.append(int(input_line[1]))

    elif command == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif command == "size":
        print(len(stack))



    elif command == "empty":
        print(0 if stack else 1)


    elif command == "top":
        print(stack[-1] if stack else -1)







