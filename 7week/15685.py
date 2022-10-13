r,c,t = map(int,input().split())

room = [list(map(int,input().split())) for _ in range(r)]

# 가장 먼저 공기 청정기 위치 찾아주기
up, down = 0, 0
for i in range(r):
    if room[i][0] == -1:
        up = i
        down = i+1 
        break

def spread():
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    temp = [ [0] * c for _ in range(r)]
    temp[up][0] = -1
    temp[down][0]=-1
    for i in range(r):
        for j in range(c):
            if room[i][j] >0 :
                tmp = room[i][j]//5
                tmp_t= 0
                for k in range(4):    
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if 0<=nx<r and 0<=ny<c and temp[nx][ny]!=-1:
                        temp[nx][ny]+= tmp
                        tmp_t += tmp
                temp[i][j]+= room[i][j]-tmp_t
    print(temp)
    return temp

       
def clean_up():
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]
    d = 0
    before = 0
    x,y = up,1
    while True:
        nx = x+dx[d]
        ny = y+dy[d]
        if x == up and y ==0:
            break
        if nx <0 or nx>= r or ny<0 or ny>=c:
            d +=1
            continue
        # print(x,y)
        room[x][y], before = before, room[x][y]
        x,y = nx, ny

def clean_down():
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    d = 0
    before = 0
    x,y = down,1
    while True:
        nx = x+dx[d]
        ny = y+dy[d]
        if x == down and y ==0:
            break
        if nx <0 or nx>= r or ny<0 or ny>=c:
            d +=1
            continue
        room[x][y], before = before, room[x][y]
        x,y = nx, ny

for _ in range(t):
    room = spread()
    print(room)
    clean_up()
    clean_down()
answer = 0
for i in range(r):
    for j in range(c):
        if room[i][j]>0:
            answer+= room[i][j]
print(room)
print(answer)