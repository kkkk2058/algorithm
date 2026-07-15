n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

# curr_v = False

graph = [[] for _ in range(n+1)]

for u,v in edges:
    graph[u].append(v)
    graph[v].append(u)

# print(graph)

visited = [False] * (n+1)
visited[1] = True


def dfs(vertex):
    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            # print(visited)
            visited[curr_v] = True
            dfs(curr_v)

dfs(1)
print(sum(visited)-1)