
def mov_dice(dice, move):
    a, b, c, d, e, f = dice[1], dice[2], dice[3], dice[4], dice[5], dice[6]
    if dir == 1: #동
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = d, b, a, f, e, c

    elif dir == 2: #서
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = c, b, f, a, e, d

    elif dir == 3: #북
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = e, a, c, d, f, b

    else:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = b, f, c, d, a, e

n, m , x, y, c = map(int,input().split())

dice = {i : 0 for i in range(1,7)}
# dice는 123456 그림과 같이 진행한다
dx = [0,0,-1,1]
dy = [1,-1,0,0]

arr = [ list(map(int,input().split())) for i in range(n)]

cmds = list(map(int,input().split()))

for cmd in cmds:
    temp_x = x+ dx[cmd-1]
    temp_y = y+ dy[cmd-1]
    if 0 > temp_x or temp_x>=n or 0 >temp_y or temp_y>=m:
        temp_x = x- dx[cmd-1]
        temp_y = y- dy[cmd-1]
    if  0 <= temp_x <n and 0 <=temp_y<m:
        x, y = temp_x,temp_y
        mov_dice(dice,cmd)
        if arr[x][y] != 0:
            dice[6] = arr[x][y]
            arr[x][y]=0
        else:
            arr[x][y]=dice[6]
            dice[6] = 0
        print(dice[1])
