from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    visited[v]= 1
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in range(1,n+1):
            if visited[i]== 0 and graph[v][i]==1:
                q.append(i)
                visited[i] =1

def dfs(v):
    visited2[v] = 1
    print(v, end=" ")
    for i in range(1,n+1):
        if visited2[i]==0 and graph[v][i]==1:
            dfs(i)

n, m, s = map(int,input().split())

visited = [0] * (n+1)
visited2 = [0] * (n+1)
graph =[[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    graph[a][b] = graph[b][a] =1

dfs(s)
print()
bfs(s)
