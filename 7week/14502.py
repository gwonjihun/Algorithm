from collections import deque
import copy

def bfs():
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    q = deque()
    tmp_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j]==2:
                q.append((i,j))
    
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx <0 or nx>=n or ny<0 or ny>=m:
                continue
            if tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny]=2
                q.append((nx,ny))

    global answer
    cnt = 0

    for i in range(n):
        cnt += tmp_graph[i].count(0)
    answer = max(cnt,answer)

def build_walls(cnt):
    if cnt == 3:
        bfs()
        return
    else:
        for i in range(n):
            for j in range(m):
                if graph[i][j]==0:
                    graph[i][j]=1
                    build_walls(cnt+1)
                    graph[i][j]=0
n, m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

answer = 0
build_walls(0)
print(answer)