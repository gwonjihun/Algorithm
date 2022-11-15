start, end = map(int,input().split())

dp = [-1]* (end+1)
ablity = list(map(int,input().split()))

# i는 최종 목적지를 의미
for i in range(start,end+1):
    if i == start:
        dp[i]=0
        continue
    # 예를 들어 능력치는 1 , 3 , 5가 있고
    # 8에 숨어있으면
    # 만약에 dp[8-1] or dp[8-3] or dp[8-5]가 0이 아니면?
    # 거기서 +1을 하면 찾아지는거고
    # 그렇다면 index out of range를 잡아주는 예외처리가 필요하겠고
    for j in range(0,3):
        if dp[i-ablity[j]]>=0:
            dp[i] = dp[i-ablity[j]]+1
    # for j in range(0,3):
print(dp)
print(dp[-1])
