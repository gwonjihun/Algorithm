n , m = map(int,input().split())

arr = [ int(input()) for _ in range(n)]

dp = [10001]* (m+1)
 # 최소값을 구하므로 dp배열에 최대값 이상의 값으로 저장
dp[0] = 0
for i in range(n):
    for j in range(1,m+1): 
        if j-arr[i]>=0:
            # j-arr[i]가 -인경우 배열의 인덱스 접근이 불가하게 설정해야함
            if dp[j - arr[i]] != 10001:
                # dp[j-arr[i]]가 존재하는 경우를 확
                dp[j] = min(dp[j],dp[j-arr[i]]+1)

print(dp)
if dp[m] ==10001:
    print(-1)
else:
    print(dp[-1])