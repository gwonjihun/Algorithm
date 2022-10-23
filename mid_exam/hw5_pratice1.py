import heapq
import sys
INF = 1e10

n, m = map(int, input().split())
# 시작 노드 1로 설정
start = 1
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append((b, 1))
graph[b].append((a, 1))


def dijkstra(start) :
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q : # 큐가 비어있지 않다면
    # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(q)
    # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist :
            continue
    # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

# 최단 거리가 가장 먼 노드 번호(숨을 헛간의 번호)
max_node = 0
# 도달할 수 있는 노드 중에서, 최단 거리가 가장 먼 노드와의 최단 거리
max_distance = 0
result = []

for i in range(1, n + 1) :
    if max_distance < distance[i] :
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif max_distance == distance[i] :
        result.append(i)

print(max_node, max_distance, len(result))