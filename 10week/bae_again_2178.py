from collections import deque
import queue


def split_input(ins):
    return [ int(i) for i in ins]

def dfs(x,y):
    dx= [1,-1,0,0]
    dy=[0,0,1,-1]

    qu = deque()
    qu.append((x,y))

    while qu:
        x,y = qu.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y+ dy[i]

            if 0<=nx<n and 0<=ny<m:
                if arr[nx][ny]==1:
                    arr[nx][ny] += arr[x][y]
                    qu.append((nx,ny))

    return arr[n-1][m-1]

n, m = map(int,input().split())

arr = [split_input(input()) for _ in range(n)]


print(dfs(0,0))
