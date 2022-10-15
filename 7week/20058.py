from collections import deque

n , q = map(int,input().split())

board_len = 2**n

board = [list(map(int,input().split())) for _ in range(board_len)]
L_list = list(map(int,input().split()) )
dx =[0,0,1,-1]
dy =[1,-1,0,0]
def rotate_and_melting(board,len_board,L):
    new_board = [[0]*len_board for _ in range(len_board)]

    r_size = 2**L
    # 2**L격자 크기로 돌린다
    for y in range(0,len_board,r_size):
        for x in range(0,len_board,r_size):
            for i in range(r_size):
                for j in range(r_size):
                    new_board[y+j][x+r_size-i-1]=board[y+i][x+j]
    # for i in range(len_board):
    #     print(board[i])    
#  00->11 01 -> 10 -> 

    board = new_board
    # print('______________________________')
    # for i in range(len_board):
    #     print(board[i])    
    # print('______________________________')

    melting_list=[]
    for i in range(0,len_board):
        for j in range(0,len_board):
            ice_count=0
            for d in range(4):
                nx = i+dx[d]
                ny = j+dy[d]

                if nx<0 or  ny<0 or nx>=len_board or ny>=len_board:
                    continue
                elif board[nx][ny]>0:
                    ice_count+=1
            if ice_count<3 and board[i][j]!=0:
                melting_list.append((i,j))

    for i,j in melting_list:
        board[i][j]-=1

    # # board 출력문
    # for i in range(len_board):
    #     print(board[i])    

    # print('______________________________')
    # for i in range(len_board):
    #     print(new_board[i])
    # 녹이는거는 끝이났음
    return board
def bfs(board, len_board):
    visited = [[False]*len_board for _ in range(len_board)]
    ice_sum = 0
    max_area_count = 0
    for i in range(len_board):
        for j in range(len_board):
            area_count = 0
            if visited[i][j] or board[i][j]==0:
                continue
            q= deque()
            q.append((i,j))
            visited[i][j]=True
            while q:
                x, y = q.popleft()

                ice_sum+=board[x][y]
                area_count+=1
                for d in range(4):
                    nx,ny = x+dx[d], y+dy[d]
                    # 배열의 외부에 대한 예외처리완료
                    if nx<0 or ny<0 or nx>=len_board or ny>=len_board:
                        continue
                    if visited[nx][ny]==True:
                        continue
                    if board[nx][ny]!=0 and visited[nx][ny]==False :
                        q.append((nx,ny))
                        visited[nx][ny]=True
            max_area_count = max(max_area_count, area_count)
    print(ice_sum)
    print(max_area_count)




for L in L_list:
    board = rotate_and_melting(board,board_len,L)

bfs(board=board,len_board=board_len)