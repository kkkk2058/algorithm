
import sys
from collections import deque


N, M, V = map(int, sys.stdin.readline().split())
#  map, int 쓰는이유 그냥 input split 만 쓰면 문자열로 저장되므로 
# map(int)를 사용하여 정수형으로 저장한다.

graph = [[] for _ in range(N+1)]

# graph의 내부 모습
# graph = [
#     [], # graph[0] : 보통 안 씀
#     [], # graph[1] : 1번 정점과 연결된 친구들 목록
#     [], # graph[2] : 2번 정점과 연결된 친구들 목록
#     [], # graph[3] : 3번 정점과 연결된 친구들 목록
#     [], # graph[4] : 4번 정점과 연결된 친구들 목록
# ]


# 간선끼리 연결 
for _ in range(M):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort()


# 지났는지 안지났는지 초기화
visted_dfs = [False] * (N + 1)
visted_bfs = [False] * (N + 1)


# 지났는지 안지났는지 확인
def dfs(V):
    visted_dfs[V] = True
    # (, end="") 줄바꿈
    print(V, end=" ")
    for i in graph[V]:
        if not visted_dfs[i]:
            dfs(i)


def bfs(V):
    visted_bfs[V] = True
    queue = deque([V])

    while queue:
        i = queue.popleft()
        print(i, end=" ")
        for j in graph[i]:
            if not visted_bfs[j]:
                queue.append(j)
                # 큐에 1이 다 돌고나서 1에 2,3 이 연결되어있으면
                # 2,3에 대한 큐도 돌아가야됨 (while문)
                visted_bfs[j]=True


dfs(V)
print()
bfs(V)
