n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

dp=[0]* (n+1)

dp[0] = arr[0]

dp[1] = dp[0]+arr[1]

dp[2] = max(arr[2]+dp[0],arr[2]+arr[1],dp[1])

for i in range(3,n):
    # i- 1을 안먹는 경우
    # 
    dp[i] = max(arr[i]+dp[i-2],arr[i]+arr[i-1]+dp[i-3],dp[i-1])

print(dp[n-1])