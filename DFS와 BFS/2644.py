import sys

n = int(input())

x1, y1 = map(int,sys.stdin.readline().split())
#split() 잊지말자

m = int(input())
graph = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)


# 0번 사람이 없고 비워져있으므로 n번째 사람은 n+1 리스트에 들어가게 된다 따라서 하나 더 만들어줘야됨
visted = [False] * (n + 1)
result = -1

def dfs(k,depth):
        global result
        visted[k] = True
        
        if k == y1:
              result = depth
              return
        
        for i in graph[k]:
              if not visted[i]:
                dfs(i, depth+1)

# 단순히 count 를 올리는게 아니라 depth를 설정해서 depth가 오히려 줄어드는 경우 올라갔다 내려가는 경우 방지
dfs(x1,0)    
        
print(result)


        #                 1                       4
        #         2             3                 5
        # 7       8       9 
# graph = list(map(int,sys.stdin.readine().split()))