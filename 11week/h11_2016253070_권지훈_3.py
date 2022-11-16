n, m = map(int,input().split())
arr = list(map(int,input().split()))
visited = []
for i in range(0,len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i] == arr[j]:
            continue
        x = (arr[i],arr[j])
        visited.append(x)

print(visited)
print(len(visited))