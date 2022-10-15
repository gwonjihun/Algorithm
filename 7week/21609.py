from collections import deque
import grp

rainbow = 0
black = -1
empty =-2

dx=[0,0,1,-1]
dy=[1,-1,0,0]

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
groups = {}
answer = 0

def select_group():
    global groups, graph
    visited = [[False]* n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] in (rainbow,black,empty): continue
            if not visited[i][j]:
                visited[i][j]= True
                groups[(i,j)] = []

                # q = 
# 중력 적용시 -1은 움직임이 없다.
# 그룹을 제거하면 제거된 배열에 m+1값을 적용해서 해당 부분은 내려갈수 있는 부분을 의미해준다
# rotate은 

# 먼저 배열의 바닥에서 부터 조회를 시작한다
# 해당 값이 -1이면 움직임 없이 넘어가도록 진행
# 해당 값이 -2이면 빈값이므로 무시
# 나머지 값의 경우 다음 if문으로 아래 배열 값이 -2일때만 교체하도록한다
# 
def gravity():
    global graph
    temp =0
    for i in range(n-1,-1,-1):
        for j in range(n):
            temp_i = i
            while temp_i > 0 and graph[temp_i][j]==-2:
                temp_i -= i
            if temp_i != i and graph[temp_i][j] != -1:
                temp= graph[temp_i][j]
                graph[temp_i][j]=-2
                graph[i][j]=temp
        
    return
            