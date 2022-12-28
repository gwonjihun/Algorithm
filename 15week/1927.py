import sys
import heapq
n = int(sys.stdin.readline())
q = []
result = []
for _ in range(n):
    x = int(sys.stdin.readline())

    if not x:
        try:
            result.append(heapq.heappop(q))
        except:
            result.append(0)
        # pop 동작
    else:
        # 푸쉬 동작을 진행한다
        heapq.heappush(q,x)        

print('\n'.join(map(str,result)))