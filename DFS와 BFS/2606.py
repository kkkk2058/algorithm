from collections import deque
import sys

N = int(input())

S = int(input())

# queue = deque()

graph = [[] for _ in range(N+1)]

# for i in range(N):
#     queue.append(i+1)

# [1,2,3,4,5,6,7]


for i in range(S):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,N+1):
    graph[i].sort()

# 이렇게만 구분하면 1,2,5 1레벨까지는 연결되는데 2,3, 5,6 2레벨까지는 연결이 안돼
# 1,2,3,5,6
# 4,7
# print( graph[1])

visted = [False] * (N + 1)
queue = deque([1])
# 큐에 시작노드를 넣어주어야 한다

visted[1] = [True]
count = 0

while queue:
    i = queue.popleft()
    for j in graph[i]:
        if not visted[j]:
            visted[j] = [True]
            queue.append(j)
            count +=1

print(count)

