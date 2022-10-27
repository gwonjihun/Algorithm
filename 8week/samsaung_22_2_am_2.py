n, m, k = map(int,input().split())

weapon = [
    [[] for _ in range(n)]
    for _ in range(n)
]
for i in range(n):
    lists =list(map(int,input().split()))
    for j in range(n):
        if lists[j]!=0:
            weapon[i][j].append(lists[j])
player = []
# [(x,y,direction,player, weapon,point)]
for _ in range(m):
    x,y,d,w, = map(int,input().split())
    player.append([x,y,d,w,0,0])
print(weapon)
print(player)



dx = [-1,0,1,0]
dy = [0,1,0,-1]

# move를 이동하고서 
def loser_move():
    pass
def winner():
    pass
def war(idx_1,idx_2):
    if player[idx_1][3]+player[idx_1][4] > player[idx_1][3]+player[idx_1][4]:
        return idx_1,idx_2
    elif player[idx_1][3]+player[idx_1][4] == player[idx_1][3]+player[idx_1][4]:
        if player[idx_1][3]> player[idx_2][3]:
            return idx_1, idx_2
        else:
            return idx_2, idx_1
    else:
        return idx_2, idx_1
        
def move(idx):
    x,y,dir,_,_,_ = player[idx]
    nx = x + dx[dir]
    ny = y + dx[dir]
    if nx <0 or ny <0 or nx>=n or ny>=n:
        d = d+2%4

for i in range(k):
    for j in range(m):
        move(j)

for i in range(m):
    print(player[i][5], end=' ')