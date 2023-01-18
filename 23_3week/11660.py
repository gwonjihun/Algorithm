import sys
input = sys.stdin.readline
# 이게 진행되야하는 이유 : 만약에 배열의 길이가 100,000이면 입력부터 타임 아웃
n,m = map(int,input().split())

dp = [ [0 for _ in range(n+1)] for _ in range(n+1)]
s = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1] - dp[i][j] + s[i][j]

for i in range(m):
    s1,s2, e1,e2 = map(int,input().split())
    print(dp[e1][e2]-(dp[s1-1][e2]+dp[e1][s2-1]-dp[s1-1][s2-1]))