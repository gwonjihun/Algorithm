from math import inf


n = int(input())
m = int(input())

graph = [[inf]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            graph[i][j]==0

for _ in range(m):
    u,v,c = map(int,input().split())
    graph[u][v]= min(c,graph[u][v])

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(1, n+1):
    for j in range(1,n+1):
        if graph[i][j] == inf:
            print('0', end=' ')
        elif i==j:
            print('0', end=' ')
        else:
            print(graph[i][j],end=' ')
    print()