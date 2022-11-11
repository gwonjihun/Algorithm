n = int(input())

dp = [[-1 for _ in range(n)] for _ in range(n)]

land = [list(map(int,input().split())) for _ in range(n)]

print(land)

def dfs(start,end):
    if dp[start][end]!=-1:
        return dp[start][end]
    if start == n-1:
        if(land[n-1][0] -land[end][0]<=land[n-1][1]) :
            dp[start][end] = 1
            return dp[start][end]
        else:
            dp[start][end] = 0
            return dp[start][end]
    elif end == n-1:
        dp[start][end] = 0
        return dp[start][end]

    mp = max(start,end)+1
    dp[start][end]=0
    # print('-------------------------------------------',start, end)
    for i in range(mp,n):
        # print('first i :',i,n)
        # print(land[i][0]-land[start][0], land[start][1])
        if land[i][0]-land[start][0] <= land[start][1]:
            a = dfs(i,end)
            # print(a)
            dp[start][end] += a
            dp[start][end] %=1000

    # print('*****************************************',start,end)
    for i in range(mp,n):
        # print(land[i][0]-land[start][0])
        if land[i][0]-land[end][0] <= land[i][1] and land[i][2]==1:
            a =  dfs(start,i)
            # print(a)
            dp[start][end] +=a
            dp[start][end] %=1000
            

    return dp[start][end]


print(dfs(0,0))
# print(dp)
