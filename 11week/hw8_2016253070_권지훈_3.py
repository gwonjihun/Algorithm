n, m = map(int,input().split())
arr = list(map(int,input().split()))
visited = []

# 2중 for문은 n의 개수 1000개이므로 시간 초과 문제 없음
# j는 i+1 이므로 같은 번호의 볼링공 선택 제외
for i in range(0,len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i] == arr[j]:
            continue
        x = (arr[i],arr[j])
        visited.append(x)

print(visited)
print(len(visited))