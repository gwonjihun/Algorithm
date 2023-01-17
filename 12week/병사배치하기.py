n = int(input())

arr = list(map(int,input().split()))

dp= [1] * n
#  15 14 13 16 12 10
#  15 11 4 8 5 2 4
#  i는 병사의 마지막 인덱스
for i in range(n):
    # 여기서는 i전까지의 병력들 중 i에 들어갈 수 있는 병력을 의미한다..?
    # 이거 좀 이상한데? 
    for j in range(i):
        print( i , j )
        if arr[j]>arr[i]:
            dp[i] = max(dp[i],dp[j]+1)
print(dp)
print(n-max(dp))