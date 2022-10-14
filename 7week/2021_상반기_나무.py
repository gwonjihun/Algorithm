# n 격자 크기 , m 박멸이 진행되는 년수, k대각선의 길이, c는 제초제가 남아있는 년수

# 먼저 나무가 성장하고 그뒤에 번식한다 
def step_oen():
    dxs, dys = [-1,1,0,0], [0,0,1,-1]

    for i in range(n):
        for j in range(n):
            if graph[i][j]<=0:
                continue

            cnt = 0
            for dirs in range(4):
                nx = i+ dxs[dirs]
                ny = j+ dys[dirs]
                if nx < 0 or ny <0 or nx>= n or ny >= n:
                    continue
                if graph[nx][ny]>0:
                    cnt+=1
            graph[i][j]+= cnt
    print("step one")
    print(graph)


# 2단계 : 기존에  있었던 나무를 기준으로 상하좌우로 나무가 번식을 하는데
# 제초제, 벽, 나무가 있는 부분은 제외하고 번식하며 번식되는 초기 값은
# 기존 나무의 길이/ /번식 가능한 나무의 칸
def step_two():
    global graph_add_tree
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for i in range(n):
        for j in range(n):
            graph_add_tree[i][j]=0

    for i in range(n):
        for j in range(n):
            if graph[i][j]<=0:
                continue

            cnt = 0
            for nd in range(4):
                nx = i+dx[nd]
                ny = j+dy[nd]
                if nx < 0 or ny <0 or nx>= n or ny >= n:
                    continue
                if graph_anti[nx][ny]:
                    continue
                if graph[nx][ny]==0:
                    cnt+=1
                
            for nd in range(4):
                nx = i+dx[nd]
                ny = j+dy[nd]
                if nx < 0 or ny <0 or nx>= n or ny >= n:
                    continue
                if graph_anti[nx][ny]:
                    continue
                if graph[nx][ny]==0:
                    graph_add_tree[nx][ny] += graph[i][j]//cnt

    for i in range(n):
        for j in range(n):
            graph[i][j] += graph_add_tree[i][j]
    print("step two")
    print(graph)
# 3번재 나무 박멸하기
# 가장 먼저 나무 박멸이 잘되는 위치부터 찾는다
# 잘되는 위치를 파악하면 해당 위치를 기준으로 해서 제초제 뿌리기
# 제초제는 1년이 지날때마다 1씩 감소시켜준다
def step_three():
    global total

    dx = [1,-1,-1,1]
    dy = [1,-1,1,-1]

    max_delete, max_x,max_y = 0,0,0

    for i in range(n):
        for j in range(n):
            # 여기서 모든 칸에 제초제를 뿌려본다는 가정하에 진행해보면서 del값을
            # 찾고 그 후에 del값이 max값 보다 크면 변경해준다.
            if graph[i][j]<0:
                continue
            
            cnt = graph[i][j]
            for dirs in range(4):
                nx = i
                ny = j
                for _ in range(k):
                    nx = nx+dx[dirs]
                    ny = ny+dy[dirs]

                    if nx < 0 or ny <0 or nx>= n or ny >= n:
                        break
                    if graph[nx][ny]<=0:
                        break
                    cnt+= graph[nx][ny]

            if max_delete< cnt:
                max_delete = cnt
                max_x, max_y = i , j

    total += max_delete
    # 여기까지해서 최고위치를 찾았어 그러면
    # 이제 제초제 두기
    # 제초제 두는 곳의 나무들 다 죽이기, anti에 제초제의 수명 작성
    if graph[max_x][max_y]>0:
        graph[max_x][max_y]=0
        graph_anti[max_x][max_y]= c
       
        for i in range(4):
            nx, ny = max_x, max_y    
            for _ in range(k):
                nx, ny = nx+dx[i], ny+dy[i]
                if nx < 0 or ny <0 or nx>= n or ny >= n:
                    break
                if graph[nx][ny] < 0: 
                    break
                if graph[nx][ny] == 0:
                    graph_anti[nx][ny] = c
                    break

                graph[nx][ny]=0
                graph_anti[nx][ny]=c
    
    print(total)



def delete_anti():
    for i in range(n):
        for j in range(n):
            if graph_anti[i][j]>0:
                graph_anti[i][j] -= -1


n, m, k, c = map(int,input().split())

graph = [ list(map(int,input().split())) for _ in range(n)]

graph_anti = [ [0]*n for _ in range(n)]
graph_add_tree = [[0] * n for _ in range(n)]
# print(graph_add_tree)
total = 0 # 박멸된 나무 갯수

for _ in range(m): # 여기서 박멸이 m번 시도한다
# 다음은 나무를 최대한 잡을 수 있는 제초제 범위선정
# 제초제 뿌림
#  다음년도로 진행
    # print(graph)
    step_oen()
    # print(graph)
    step_two()
    delete_anti()
    step_three()

print(total)