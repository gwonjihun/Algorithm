#  a-b b-c c-d d-e라는 의미는 그래프의 깊이가 5가되느냐는것을 의미 dfs로 cnt가 5가 되면 stop때리자
n, m = map(int,input().split())

arr = [[] for _ in range(n)]
visit = [False]* n
ans = False


for _ in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(index, cnt):
    global ans
    visit[index] = True
    if cnt == 4:
        ans = True
        return
    for j in arr[index]:
        if not visit[j]:
            visit[j] = True
            dfs(j,cnt+1)
            visit[j] = False


for i in range(n):
    dfs(i,0)
    visit[i] = False

    if ans:
        break


if ans:
    print(1)
else:
    print(0)