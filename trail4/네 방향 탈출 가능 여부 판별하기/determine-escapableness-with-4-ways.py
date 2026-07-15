from collections import deque


n, m = map(int, input().split())


a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [[0]*m for _ in range(n)]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or a[x][y] == 0:  # 뱀이면 못 감
        return False
    return True



def bfs():
    q = deque()
    dxs = [-1,0,1,0]
    dys = [0,1,0,-1]

    q.append((0, 0))          # ① 시작점 넣기
    visited[0][0] = 1         # ② 시작점 방문처리


    #동남서북
    while q:
        x,y= q.popleft()

        for dx,dy in zip(dxs,dys):
            nx , ny = x + dx , y + dy
            if can_go(nx, ny):
                visited[nx][ny] = 1
                q.append((nx, ny)) 

bfs()

print(1 if visited[n-1][m-1] else 0)