import heapq

n = int(input())
q = []
for _ in range(n):
    m = int(input())
    if m == 0:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q))
            
