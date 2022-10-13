# 4 * 2 * 4 * 4 * 1
#8 * 16 = 128

from cmath import inf
import copy


dx = [0,0,1,-1]
dy = [1,-1,0,0]
motion = [ [],
            [[0],[1],[2],[3]],
            [[0,1],[2,3]],
            [[3,0],[0,2],[2,1],[1,3]],
            [[0,1,2],[0,1,3],[2,3,0],[2,3,1]],
            [[0,1,2,3,]]
        ]
n,m = map(int,input().split())

room = [list(map(int,input().split())) for _ in range(n)]
cctv_list = []

for i in range(n):
    for j in range(m):
        if  0<room[i][j] <6:
            cctv_list.append([i,j,room[i][j]])

def fill(arr,move, x,y):
    for i in move:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if  nx <0 or ny <0 or nx>=n or ny >= m:
                break
            if arr[nx][ny]== 6:
                break
            elif arr[nx][ny] == 0:
                arr[nx][ny] = 7

        
def dfs(depth, arr):
    global count

    if depth >= len(cctv_list):
        cnt = 0
        for i in range(n):
            cnt += arr[i].count(0)
        count = min(count, cnt)
        return
    temp = copy.deepcopy(arr)
    # print(depth)
    x,y,cctv_num = cctv_list[depth]
    
    for i in motion[cctv_num]:
        fill(temp,i,x,y)
        dfs(depth+1,temp)
        temp = copy.deepcopy(arr)

count = inf
dfs(0,room)
print(count)