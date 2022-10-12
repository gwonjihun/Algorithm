n, l = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]
# 1. 1번과 2번 차이가 절대값 2이상 나면 바로 false다 
# 2. 1차이가 나는게 l길이보다 짧으면 false다
# 3. visited한 곳을 사용해야하면 false다
def check(li): ## 1차원 배열을 기준으로 판단한다
    visited = [False for i in range(n)]
    for i in range(n-1):
        if li[i]==li[i+1]:
            continue
        if abs(li[i]-li[i+1])>1:
            return False
        if li[i]>li[i+1]:
            temp = li[i+1]
            for j in range(i+1,i+l+1):
                if 0<=j<n:
                    if li[j]!= temp: return False
                    if visited[j]==True: return False # 해당부분을 경사로로 이미 사용
                    visited[j]=True
                else:
                    return False
        else:
            temp = li[i]
            for j in range(i,i-l,-1):
                if 0<=j<n:
                    if li[j]!=temp: return False
                    if visited[j]==True: return False
                    visited[j]=True
                else:
                    return False
    return True

cnt =0
for i in graph:
    if check(i):
        cnt+=1

for i in range(n):
    temp = []
    for j in range(n):
        temp.append(graph[j][i])
    if check(temp):
        cnt += 1

print(cnt)
        
            
