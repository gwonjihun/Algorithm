n = int(input())
arr = [[0]*2 for _ in range(n)]
for i in range(n):
    s, e = map(int,input().split())
    arr[i][0]=s
    arr[i][1]=e
# 회의 종료시간, 시작 시간으로 정렬
arr.sort(key= lambda x:(x[1],x[0]))
cnt= 1 
end = arr[0][1]

for i in range(1,n):
    if end<=arr[i][0]:
        cnt += 1
        end = arr[i][1]
print(cnt)