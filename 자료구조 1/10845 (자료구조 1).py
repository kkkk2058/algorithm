from collections import deque
import sys


N = int(input())
queue = deque()

for i in range(N):
    command = input().split()

    if command[0] == 'push':
        queue.append(command[1])

    elif command[0] == 'pop':
        if queue:
            print(queue.popleft()) 
        else:
            print(-1)


    elif command[0] == 'size':
        print(len(queue))

    elif command[0] == 'empty':
        print(0 if queue else 1)

    elif command[0] == 'front':
        print(queue[0] if queue else -1)

    elif command[0] == 'back':
        print(queue[-1] if queue else -1)


