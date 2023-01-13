import sys
input = sys.stdin.readline
max_cnt = 64
N, M = map(int, input().split())
chess_list = []

for i in range(N):
    chess_list.append(input().rstrip())
print(chess_list)

def check_count(start_row, start_column): #시작 위치
    W_start_cnt = 0
    for i in range(start_row, start_row+8):
        for j in range(start_column, start_column+8):
            if i % 2 == 0 :
                if j % 2 == 0:
                    if chess_list[i][j] != 'W' :
                        W_start_cnt += 1
                    
                else :
                    if chess_list[i][j] != 'B' :
                        W_start_cnt += 1
                    
            else :
                if j % 2 == 0 :
                    if chess_list[i][j] != 'B' :
                        W_start_cnt += 1
                    
                else :
                    if chess_list[i][j] != 'W' :
                        W_start_cnt += 1
                    

    return W_start_cnt

cnt = 0
for i in range(0, N-7):
    for j in range(0, M-7):
        cnt = check_count(i,j)
        if cnt < max_cnt :
            max_cnt = cnt
        elif 64 - cnt < max_cnt :
            max_cnt = 64 - cnt
        else :
            continue
print(max_cnt)