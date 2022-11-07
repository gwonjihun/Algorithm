N, M = map(int,input().split())
arr = [[0, 0]]

for _ in range(N):
    w , v = map(int,input().split())
    temp = [w,v]
    arr.append( temp )

dp = [[0]*(M+1) for _ in range(N+1)] # dp생성

for i in range(1,N+1):
    tmp_W = arr[i][0]
    tmp_V = arr[i][1]
    for j in range(1,M+1):
        if j < tmp_W:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-tmp_W]+tmp_V)

print(dp)