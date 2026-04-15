import sys
from collections import deque

m,n,h = map(int,sys.stdin.readline().split())


matrix = [[ list(map( int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h) ]

visited = [[[False] * m for _ in range(n)] for _ in range(h)] 

dx = [0,0,1,-1,0,0]
dy = [1,-1,0,0,0,0]
dz = [0,0,0,0,1,-1]

queue = deque()


def bfs(matrix,x,y):
    count = 0
    matrix[x][y][z] = 0
    queue.append((x,y,z))
    
    while queue:
        cx,cy,cz = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            nz = cz + dz[i] 
