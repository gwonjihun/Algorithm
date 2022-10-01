
lines, cell = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(lines)]

# 막대별 회전됨에 따라 생기는 모양은 1, 2, 4 경우의 수가 있으므로
# 1개의 경우는 방향성을 제외한 함수로
# 나머지 도형을 4개의 방향성이 있는 함수로 작성 후
# %2 or 0~3까지의 값 두개의 방법으로 나누어서 구현
# 배열 범위 벗어나는지 확인 후 해당 배열 값을 return
sums = -100000000
# 배열 전체를 순환하기 위한 반복문
#사각 막대

def box(tx,ty):
    if tx+1 >= lines or ty+1 >= cell :
        return 0
    
    return arr[tx][ty] + arr[tx+1][ty] + arr[tx][ty+1] +arr[tx+1][ty+1]

# 일자 막대
# direction % 2로 방향 2개 부분에 대해서만 검증
def box_2(tx,ty,direction):
        
    if direction% 2 == 0 :
        if tx + 1>= lines or tx + 2>= lines or tx + 3>= lines:
            return 0
        return arr[tx][ty] + arr[tx+1][ty] + arr[tx+2][ty] +arr[tx+3][ty]
    elif direction% 2 == 1 :
        if ty + 1 >= cell or ty + 2 >= cell or ty + 3 >= cell:
            return 0 
        return arr[tx][ty] + arr[tx][ty+1] + arr[tx][ty+2] +arr[tx][ty+3]



# ㄴ 막대
def box_3(tx,ty,direction):
    if direction == 0:
        if tx + 1 >= lines or tx + 2 >= lines or ty+1 >= cell:
            return 0
        return arr[tx][ty] + arr[tx+1][ty] + arr[tx+2][ty] + arr[tx+2][ty+1] 
    elif direction == 1:
        if tx + 1 >= lines or ty + 1 >= cell or ty+2 >= cell:
            return 0
        return arr[tx][ty] + arr[tx+1][ty] + arr[tx][ty+1] + arr[tx][ty+2]
    elif direction == 2:
        if tx + 1 >= lines or tx + 2 >= lines or ty+1 >= cell:
            return 0
        return arr[tx][ty] + arr[tx][ty+1] + arr[tx+1][ty+1] + arr[tx+2][ty+1]
    elif direction == 3:
        if tx + 1 >= lines or ty - 2 < 0 or ty-1 < 0 :
            return 0
        return arr[tx][ty] + arr[tx+1][ty] + arr[tx+1][ty-1] + arr[tx+1][ty-2]
        
# ㄴ 막대 대칭 변환
def box_3_1(tx,ty,direction):
    if direction == 0:
        if tx + 1 >= lines or ty + 2 >= cell or ty+1 >= cell:
            return 0
        return arr[tx][ty] + arr[tx+1][ty] + arr[tx+1][ty+1] + arr[tx+1][ty+2] 
    elif direction == 1:
        if tx + 1 >= lines or tx + 2 >= lines or ty+1 >= cell:
            return 0
        return arr[tx][ty] + arr[tx+1][ty] + arr[tx][ty+1] + arr[tx+2][ty]
    elif direction == 2:
        if tx + 1 >= lines or ty + 2 >= cell or ty+1 >= cell:
            return 0
        return arr[tx][ty] + arr[tx][ty+1] + arr[tx+1][ty+2] + arr[tx][ty+2]
    elif direction == 3:
        if tx + 1 >= lines or tx + 2 >= lines or ty-1 < 0 :
            return 0
        return arr[tx][ty] + arr[tx+2][ty] + arr[tx+1][ty] + arr[tx+2][ty-1]

# Z막대
def box_4(tx,ty,direction):
    if direction % 2== 0:
        if tx + 1 >= lines or tx + 2 >= lines or ty-1 < 0:
            return 0
        return arr[tx][ty] + arr[tx+1][ty] + arr[tx+1][ty-1] + arr[tx+2][ty-1] 
    elif direction % 2 == 1:
        if tx + 1 >= lines or ty+1 >= cell or ty+2 >= cell:
            return 0
        return arr[tx][ty] + arr[tx][ty+1] + arr[tx+1][ty+1] + arr[tx+1][ty+2]

# Z막대_대칭 변환
def box_4_1(tx,ty,direction):
    if direction % 2== 0:
        if tx + 1 >= lines or tx + 2 >= lines or ty+1 >= cell:
            return 0
        return arr[tx][ty] + arr[tx+1][ty] + arr[tx+1][ty+1] + arr[tx+2][ty+1] 
    elif direction % 2 == 1:
        if tx - 1 < 0  or ty+1 >= cell or ty+2 >= cell:
            return 0
        return arr[tx][ty] + arr[tx][ty+1] + arr[tx-1][ty+1] + arr[tx-1][ty+2]

# ㅜ막대
def box_5(tx,ty,direction):
    if direction == 0:
        if tx + 1 >= lines or tx + 2 >= lines or ty+1 >= cell:
            return 0
        return arr[tx][ty] + arr[tx+1][ty] + arr[tx+2][ty] + arr[tx+1][ty+1] 
    elif direction == 1:
        if tx + 1 >= lines or ty + 1 >= cell or ty+2 >= cell:
            return 0
        return arr[tx][ty] + arr[tx+1][ty+1] + arr[tx][ty+1] + arr[tx][ty+2]
    elif direction == 2:
        if tx - 1 < 0 or ty + 1 >= cell or tx+1 >= lines:
            return 0
        return arr[tx][ty] + arr[tx][ty+1] + arr[tx-1][ty+1] + arr[tx+1][ty+1]
    elif direction == 3:
        if tx - 1 < 0 or ty + 1 >= cell  or ty+ 2 >= cell :
            return 0
        return arr[tx][ty] + arr[tx-1][ty+1] + arr[tx][ty+1] + arr[tx][ty+2]


for i in range(lines):
    for j in range(cell):
        # print(f'--------i : {i}, j: {j}----------')
        # 행렬의 위치마다 4가지 방향을 기준으로 검색
        # 단 네모 막대는 모든 방향이 동일하므로 한번만 검색
        case1 = box(i,j) 
        sums = max(sums,case1)      
        # print(f'case1 : {case1} result : {sums}')
        for cur_dir in range(0,2):
            case2 = box_2(i,j,cur_dir)
            case4 = box_4(i,j,cur_dir)
            case4_1 = box_4_1(i,j,cur_dir)
            sums = max(sums,case2,case4,case4_1)
        for cur_dir in range(0,4):
            case3 = box_3(i,j,cur_dir)
            case3_1 = box_3_1(i,j,cur_dir)
            case5 = box_5(i,j,cur_dir)
            sums = max(sums,case3,case5,case3_1)
            # print(f'case2 : {case2}, case3 : {case3} result : {sums}')

print(sums)
