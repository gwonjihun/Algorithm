T = int(input())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
from collections import deque
def bfs(graph,a,b):
    que = deque()
    que.append((a,b))

    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0<= nx < m and 0<= ny < n) and graph[nx][ny]==1:
                # print(nx,ny)
                graph[nx][ny] =0
                que.append((nx,ny))
    return


for test_case in range(T):
    m, n, s = map(int,input().split())

    arr = [[0]*n for _ in range(m)]
    for _ in range(s):
        x,y = map(int,input().split())
        arr[x][y] = 1
    
    answer = 0
    
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                bfs(arr,i,j)
                answer +=1
    print(answer)