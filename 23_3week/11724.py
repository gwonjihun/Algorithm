# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
# bfs,dfs를 통해서 연결된 간선에 대해서 체크해준다
# cnt 값을 통해서 check[]에 값을 할당한다 0은 아직 미방문, 1~n은 연결 요소의 개수를 의미해준다.
# bfs로 1회 후에 check[i] 0이 아니면 continue로 넘어가게 해준다.
# 먼저 check[]을 통해서 
from collections import deque
n,m = map(int,input().split())

arr = [[] for _ in range(n)]
check = [0]*n
for _ in range(m):
    a,b = map(int,input().split())
    arr[a-1].append(b-1)
    arr[b-1].append(a-1)

cnt = 1
for i in range(n):
    if check[i] != 0:
        continue
    else:
        q = deque()
        q.append(i)
        while q:
            nx = q.popleft()
            
            if check[nx] ==0:
                for j in arr[nx]:
                    q.append(j)
            check[nx]= cnt
        cnt+=1

print(cnt-1)
