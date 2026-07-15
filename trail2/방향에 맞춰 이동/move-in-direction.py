n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]


dx = [1,0,-1,0]
dy = [0,-1,0,1]
nx,ny = 0,0
#동남서북

for i,j in zip(dir,dist):

    if i == "E":
        nx,ny= nx + dx[0]*j, ny + dy[0]*j
    if i == "S":
        nx,ny= nx + dx[1]*j, ny + dy[1]*j
    if i == "W":
        nx,ny= nx + dx[2]*j, ny + dy[2]*j
    if i == "N":
        nx,ny= nx + dx[3]*j, ny + dy[3]*j


print(nx,ny)