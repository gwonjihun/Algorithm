def fibo_dp_botup(n):
    dp = [0] * 100
    dp[1] = 1
    dp[2] = 1
    for i in range(3,n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]

dp = [0] * (100)
def fibodp_top_down(n):
    if n == 1 or n== 2:
        return 1

    if dp[n] != 0:
        return dp[n]
    dp[n] = fibodp_top_down(n-1)+fibodp_top_down(n-2)
    return dp[n]
print(fibo_dp_botup(1))
print(fibodp_top_down(4))