from collections import deque

dx, dy = [0,1,0,-1], [1,0,-1,0]

def bfs(arr,visited,time,S,G):
    deq = deque([S])
    while deq:
        x,y = deq.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<= nx< N and 0<= ny<N:
                if visited[nx][ny]==0:
                    visited[nx][ny]=1
                    time[nx][ny] = time[x][y]+arr[nx][ny]
                    deq.append((nx,ny))
                else:
                    if time[nx][ny] > time[x][y]+arr[nx][ny]:
                        time[nx][ny] = time[x][y]+arr[nx][ny]
                        deq.append((nx,ny))


for tc in range(1,int(input())+1):
    N = int(input())
    arr = list(list(map(int,input())) for _ in range(N))
    # print(arr)
    visited = [[0]* N for _ in range(N)]
    time = [[0]* N for _ in range(N)]
    S,G = [0,0], [N-1,N-1]

    bfs(arr,visited,time,S,G)
    print(f'#{tc} {time[N-1][N-1]}')