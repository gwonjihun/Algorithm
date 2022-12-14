from collections import deque



def split_input(ins):
    return [ int(i) for i in ins]

n , m = map(int,input().split())

arr = [split_input(input()) for _ in range(n)]

def bfs(x,y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx >= n or ny <0 or ny >= m:
                continue

            if arr[nx][ny]==0:
                continue
            if arr[nx][ny]==1:
                arr[nx][ny] = arr[x][y]+1
                queue.append((nx,ny))
    return arr[n-1][m-1]

print(bfs(0,0))
            
            
            