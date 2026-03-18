from collections import deque





# print(graph)

dx = [-1,1,0,0]
dy = [0,0,-1,1]



def bfs(graph,x,y,n):
    n = len(graph)
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    count = 1

    #queue 전부 돌 때 while 쓰는 것 까먹지 말기
    while queue:
        cx,cy = queue.popleft()
        for i in range(4):
            
            nx = cx +dx[i]
            ny = cy +dy[i]
            # 범위 체크를 해주지 않으면 다른 집들이랑 합쳐질 수도 있다.
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    queue.append((nx,ny))
                    graph[nx][ny] = 0
                    count+=1

    return count






# N = int(input())

# # 이건 빈 2차원 리스트를 만드는 방법이다
# graph = [[] for _ in range(N)]

# # 이건 모든 2차원 리스트를 만드는 방법이다
# for i in range(N):
#     for j in range(N):
#         graph.append((i,j))

# # 이건 숫자입력이 부터있으면 하나의 숫자로 인식한다
# graph =[]

# for i in range(N):
#     x = int(input())
#     graph.append((x))
#     for j in range(N):
#         y = int(input())
#         graph.append((y))






graph =[]
N=int(input())
for i in range(N):
    graph.append(list(map(int, input().strip())))
    #n=3, [011]     
cnt = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt.append(bfs(graph,i,j,N))

cnt.sort()

print(len(cnt))


for i in range(len(cnt)):
    print(cnt[i])