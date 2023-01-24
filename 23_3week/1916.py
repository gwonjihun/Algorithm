n = int(input())
m = int(input())

arr = [[] for _ in range(n+1)]
visited = [1e9]*(n+1)
for _ in range(m):
    a,b,c = map(int,input().split())
    arr[a].append((c,b))

s,e = map(int,input().split())
import heapq
def dijkstra(x):
    pq = []
    heapq.heappush(pq,(0,x))
    visited[x] = 0
    while pq:
        d, x = heapq.heappop(pq)

        if visited[x]<d:
            continue
        
        for nw,nx in arr[x]:
            nd = d+nw

            if visited[nx] > nd:
                heapq.heappush(pq,(nd,nx))
                visited[nx] = nd


dijkstra(s)
print(visited[e])