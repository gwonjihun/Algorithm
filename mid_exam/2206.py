from collections import deque
import queue

def split_input(ins):
    return [ int(i) for i in ins]

n , m = map(int,input().split())

visited = [ [ [0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0]=1
# 벽을 뚫을수 있는지 유무를 판단한기 위해
# 3차원을 써야한다.
arr = [split_input(input()) for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,1,-1]

def bfs(x,y,z):
    queue = deque()
    queue.append((x,y,z))

    while queue:
        a,b,c = queue.popleft()
        if a == n-1 and b == m-1:
            # 최종 목적지 도착함에 따라 최종 결과 출력해준다.
            return visited[a][b][c]         
        for i in range(0,4):
            next_x = a+dx[i]
            next_y = b+dy[i]

            # 배열 범위를 넘어가는 부분 탐색은 그냥 넘어간다.
            if next_x < 0 or next_x>= n or next_y <0 or next_y >= m:
                continue
            
            # 먼저 다음 이동할 곳이 벽이고 벽파괴 기회가 있는경우
            # 벽이고 파괴 기회 없는경우 -> 그냥 중단되면 queue에 넣지않는다
            # 다음 벽없고 방문 안했으면 걍 큐에 넣어준다.
            if arr[next_x][next_y] == 1 and c==0:
                visited[next_x][next_y][1]= visited[a][b][0]+1
                print(next_x,next_y,1,visited[next_x][next_y][1])
                queue.append((next_x,next_y,1))
            elif arr[next_x][next_y] == 0  and visited[next_x][next_y][c]==0:
                visited[next_x][next_y][c]= visited[a][b][c]+1
                
                print(next_x,next_y,c,visited[next_x][next_y][c])
                queue.append((next_x,next_y,c))

    return -1

print(bfs(0,0,0))            


#
# 잘못된 풀이
# 


# print(arr)
# dx=[-1,1,0,0]
# dy=[0,0,1,-1]
# def bfs(x,y,count,attack):

#     if arr[x][y]== 1 and attack == 0:
#         return -1
#     if arr[x][y]== 1 and attack == 1:
        
#         for i in range(0,4):
#             if x+dx[i] == n-1 and y+dy[i]== m-1:
#                 return result.append(count+1)
#             bfs(x+dx[i],y+dy[i],count+1,attack-1)
#     if arr[x][y]==0:
#         for i in range(0,4):
#             if x+dx[i] == n-1 and y+dy[i]== m-1:
#                 return result.append(count+1)
#             bfs(x+dx[i],y+dy[i],count+1,attack-1)
        
# bfs(0,0,1,1)
# if len(result) == 0:
#     print(-1)
# else:
#     print(min(result))
    
# dfs 재귀함수로 구현시 최대 반복횟수 초과로 에러발생하므로 bfs가 맞는데