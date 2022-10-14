
from collections import deque

n = int(input())
def split_strs(s):
    return [ int(i) for i in s]
town = [ split_strs(input()) for _ in range(n)]

dx =[0,0,1,-1]
dy =[1,-1, 0, 0]

def bfs(arr,i,j):
    q= deque()
    q.append((i,j))
    arr[i][j]=0
    cnt=1
    while q:
        x,y = q.popleft()
        for dir in range(0,4):
            nx = x +dx[dir]
            ny = y +dy[dir]

            if nx<0 or nx>=n or ny<0 or ny >= n :
                continue
            if arr[nx][ny]==1:
                arr[nx][ny]=0
                q.append((nx,ny))
                cnt+=1

    return cnt

count = []
for i in range(n):
    for j in range(n):
        if town[i][j]==1:
            count.append(bfs(town,i,j))

count.sort()
print(len(count))
for i in count:
    print(i)