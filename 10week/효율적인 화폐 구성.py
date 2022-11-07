n , m = map(int,input().split())

arr = [ int(input()) for _ in range(n)]

dp = [10001]*10001
 # 최소값을 구하므로 dp배열에 최대값 이상의 값으로 저장
dp[0] = 0
for i in range(1,n): #arr 배열에 있는 값들만 활용하기 위해서
    for j in range(arr[i],m+1): 
        if dp[j - arr[i]] != 10001:
            dp[j] = min(dp[j],dp[j-arr[i]]+1)

print(dp[:m+1])