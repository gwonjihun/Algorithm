n = int(input())

arr = list(map(int,input().split()))

dp= [1] * n
#  15 14 13 16 12 10
for i in range(n):
    for j in range(i):
        print( i , j )
        if arr[j]>arr[i]:
            dp[i] = max(dp[i],dp[j]+1)
print(dp)
print(n-max(dp))