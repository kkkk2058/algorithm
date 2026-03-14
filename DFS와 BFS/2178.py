import sys
from collections import deque
N,M =map(int, sys.stdin.readline().split())

graph = []

# 1. [[0] * M] * N (얕은 복사 발생)
# 이 코드는 파이썬에게 다음과 같이 명령하는 것과 같습니다.

# [0] * M을 계산해서 리스트 객체를 딱 하나 만든다. (예: 주소값이 0x100인 리스트)

# 그 객체(0x100)를 N번 복사해서 큰 리스트에 담는다.

# 결과: 모든 행이 0x100이라는 동일한 메모리 주소를 가리킵니다. 그래서 하나를 바꾸면 다 같이 바뀝니다.

# 2. [[0] * M for _ in range(N)] (독립된 객체 생성)
# 이 코드는 **"루프(for문)를 돌면서 매번 새로운 리스트를 만들어라"**라는 명령입니다.

# for문의 첫 번째 루프: [0] * M을 실행해 리스트를 만든다. (주소: 0x201)

# for문의 두 번째 루프: [0] * M을 다시 실행해 리스트를 만든다. (주소: 0x202)

# 이 과정을 N번 반복한다.

# 결과: 각 행이 서로 다른 메모리 주소를 가진 별개의 리스트 객체가 됩니다.

# for i in range(N):
#     graph = list(map(int,sys.stdin.readline().split()))

graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

# 입력: "101\n".strip() 없음: "101\n" 그대로 유지list() 변환 후: ['1', '0', '1', '\n']결과: 리스트의 마지막 요소로 **\n**이라는 불필요한 문자가 들어갑니다. **리스트의 길이는 $M+1$**이 되어버립니다.

# print(graph)



def bfs(x,y):
    # 조이스틱, 상하좌우 움직임 만들어주기
    dx = [-1, 1 ,0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx< 0 or nx>= N or ny <0 or ny>= M:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1 :
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

    # 파이썬의 리스트는 숫자를 0부터 센다.
    return graph[N-1][M-1]

print(bfs(0,0))