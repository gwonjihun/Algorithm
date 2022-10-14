#  1. 배열 안에 있는 모든 바이러스의 자표를 x,y로 찾아낸다
#  2. 조합을 이용해서 3개를 선택하여 for문이 돌아가게한다
#  3. dfs에서 while true로 해놓고 처음 q에는 모든 바이러스를 먼저 넣어준다
#  4. 모든 바이러스에 대해서 q에서 하나꺼내어 1초라는 기준의 동작을 진행한다
#  5. q가 모두 끝나고 열단위로 0이 남아 있는지를 확인한다.
#  6. 시간 측정 방법 초기 q로 한바퀴를 돌리고서 cnt를 1로 증가시킨다
#  7. 
from collections import deque
from itertools import combinations
import copy
n , b = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

virus = []
for i in range(n):
    for j in range(n):
        if graph[i][j]==2:
            virus.append((i,j))

def bfs(cmb,temp_graph):
    print('-----------------------')
    for i in range(n):
        print(temp_graph[i])

    print('-----------------------')
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    q = deque()
    visited = []
    for i in cmb:
        q.append(i)
        visited.append(i)
    time = 0
    while q:
        flag = 1
        for i in range(n):
            if temp_graph[i].count(0) != 0:
                flag =0
        if flag == 1:
            return time
        for _ in range(len(q)):
            x,y = q.popleft()
            for i in range(0,4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx< 0 or ny < 0 or nx >=n or ny>= n:
                    continue
                if temp_graph[nx][ny] in [0,2] and ((nx,ny) not in visited):
                    temp_graph[nx][ny]= 3
                    visited.append((nx,ny))
                    q.append((nx,ny)) 
        time += 1
    print('-----------------------')
    for i in range(n):
        print(temp_graph[i])

    print('-----------------------')
    
    for i in range(n):
        if temp_graph[i].count(0) != 0:
            return 1e9
    return time

answer = 1e9
for cmb in combinations(virus,b):
    answer = min(answer,bfs(cmb,graph))

if answer == 1e9:
    print(-1)
else:
    print(answer)