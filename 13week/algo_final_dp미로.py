n, m= map(int, input().split())

array = [list(map(int, input().split())) for _ in range(n)]

 

# Dynamic Programming을 위한 2차원 DP 테이블 초기화

d = [[-1]*(m) for _ in range(n)]

d[0][0] = array[0][0]

 

# Dynamic Programming (Bottom-up) 

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0 :
            continue
        if i == 0 :
            d[i][j] = array[i][j]+ d[i][j-1]
        elif j == 0 :
            d[i][j] = d[i-1][j]+ array[i][j]
        else:
            d[i][j] = array[i][j]+ max(d[i-1][j-1],d[i-1][j],d[i][j-1])
        

print(d[n-1][m-1])