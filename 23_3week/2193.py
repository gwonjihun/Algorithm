# 1
# 10
# 101, 100,
# 1010, 1001, 1000
# 10000, 10001, 10010, 10100, 10101
# 100000, 100001, 100010, 100100, 100101, 101000, 101001,101010
# 1, 1, 2, 3, 5, 8개다
n = int(input())

dp =[0,1,1]
for i in range(3,91):
    dp.append(dp[i-2]+dp[i-1])

print(dp[n])