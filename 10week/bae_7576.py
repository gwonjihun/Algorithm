from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
m, n = map(int,input().split())

arr= [ list(map(int,input().split())) for _ in range(n)]
s = deque()
result = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            s.append([i,j])

def bfs():
    while s:
        x,y = s.popleft()
        for i in range(4):
            nx, ny = dx[i]+x,dy[i]+y

            if 0<= nx < n and 0<=ny <m and arr[nx][ny]==0:
                arr[nx][ny]=arr[x][y]+1
                s.append([nx,ny])


bfs()
for i in arr:
    for j in i:
        if j==0:
            print(-1)
            exit()
    
    result = max(result,max(i))
print(result-1)