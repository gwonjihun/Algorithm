from collections import deque

N, M, V = map(int,input().split())
visit_list =[0] * (n + 1)

def bfs(v):
    q = deque()
    q.append(v)
    visit_list[v]=1
    while q:
        v = q.popleft()
        print(v, end= " ")
        for i in range(1,N+1):
            #if visit_list[i]==0 and graph[v][i]==1:
            q.append(i)
            visit_list[i]=1

arrs = [[0 for _ in range(N+1)] for _ in range(N+1)]
print(arrs)
#DFS

#BPS