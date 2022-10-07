n, s = map(int,input().split())

arr = list(map(int,input().split()))
cnt = 0
def dfs(sum, idx):
    global cnt
    if idx >= n:
        return
    sum += arr[idx]
    if sum == s:
        cnt += 1
    dfs(sum, idx+1)
    dfs(sum-arr[idx],idx+1)

dfs(0,0)
print(cnt)