from collections import deque
# 가장 먼저 해야할 일 a,b의 인덱스를 찾아주기
# 
# 먼저 움직임은 끝까지 움직이게 되
# 닌깐 무브의 중단은 움직이는 방향쪽에서 #을 만나야함
# 
def split_input(inputs):
   return [i for i in inputs]

n,m = map(int,input().split())

arr = [split_input(input()) for _ in range(n)]
R_x = 0
R_y = 0
B_y = 0
B_x = 0
R_c = 0
B_c = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(n):
    if R_c == 1 and B_c == 1:
        break
    for j in range(m):
        if R_c == 1 and B_c == 1:
            break
        if arr[i][j] == 'R':
            R_x, R_y = i,j
            R_c=1 
        elif arr[i][j] == 'B':
            B_x, B_y = i,j
            B_c= 1

def bfs(rx,ry,bx,by):
    q = deque()
    q.append((rx,ry,bx,by))
    visitied = []
    visitied.append((rx,ry,bx,by))
    count = 0
    while q:
        for al in range(len(q)):
            print(al, len(q))
            rx,ry,bx,by=q.popleft()
            if count > 10:
                print(-1)
                return
            # print(rx,ry,bx,by)
            if arr[rx][ry]=='O':
                print(count)
                print('mid')
                return
            for i in range(0,4):
                nrx,nry= rx,ry
                while True:
                    nrx += dx[i]
                    nry += dy[i]
                    if arr[nrx][nry]=='#':
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                    if arr[nrx][nry]=='O':
                        break
                nbx,nby = bx,by
                while True:
                    nbx += dx[i]
                    nby += dy[i]
                    if arr[nbx][nby]=='#':
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                    if arr[nbx][nby]=='O':
                        break
                if arr[nbx][nby]=='O':
                    continue
                if nrx == nbx and nry == nby:
                    if abs(nrx-rx) + abs(nry-ry) > abs(nbx-bx)+abs(nby-by):
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if (nrx,nry,nbx,nby) not in visitied:
                    visitied.append((nrx,nry,nbx,nby))
                    q.append((nrx,nry,nbx,nby))
        count += 1

    print(-1)

bfs(R_x,R_y,B_x,B_y)
