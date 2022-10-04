wid, hi = map(int,input().split())

x,y ,d = map(int,input().split())

arr = [[0]*hi]*wid
visited = arr.copy()
visited = [[0] * hi for _ in range(wid)]
# d => 0,3,2,1 순서로 돌아야한다.
dx = [-1,0,1,0]
dy = [0,1,0,-1]

for i in range(wid):
    arr[i] = list(map(int,input().split()))
# 0이면 위 1 은 오른쪽 2는 아래 3은 왼쪽
visited[x][y]=1
count=1 
while 1:
    flag = 0
    for _ in range(4):
        next_x = x + dx[(d+3)%4]
        next_y = y + dy[(d+3)%4]
        d = (d+3)%4
        if 0<= next_x < wid and 0<= next_y < hi and arr[next_x][next_y] ==0:
            if visited[next_x][next_y]==0:
                visited[next_x][next_y]=1
                count+=1
                x=next_x
                y=next_y
                flag = 1
                break
    if flag == 0:
        if arr[x-dx[d]][y-dy[d]] == 1:
            print(count)
            break
        else:
            x,y = x-dx[d],y-dy[d]

# while 1:
#     flag = 0
#     # 4방향 확인
#     for _ in range(4):
#         # 0,3,2,1 순서 만들어주기위한 식
#         nx = r + dx[(d+3)%4]
#         ny = c + dy[(d+3)%4]
#         # 한번 돌았으면 그 방향으로 작업시작
#         d = (d+3)%4
#         if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
#             if visited[nx][ny] == 0:
#                 visited[nx][ny] = 1
#                 cnt += 1
#                 r = nx
#                 c = ny
#                 #청소 한 방향이라도 했으면 다음으로 넘어감
#                 flag = 1
#                 break
#     if flag == 0: # 4방향 모두 청소가 되어 있을 때,
#         if graph[r-dx[d]][c-dy[d]] == 1: #후진했는데 벽
#             print(cnt)
#             break
#         else:
#             r,c = r-dx[d],c-dy[d]