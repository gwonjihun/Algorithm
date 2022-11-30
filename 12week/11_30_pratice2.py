from collections import deque
n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

visited = [-1]*(n+1)
visited[x]= 0

q = deque([x])
while q:
    temp = q.popleft()
    for i in graph[temp]:
        if visited[i]==-1:
            visited[i]= visited[temp]+1
            q.append(i)

if k in visited:
    for i in range(1,n+1):
        if visited[i]==k:
            print(i)
else:
    print(-1)