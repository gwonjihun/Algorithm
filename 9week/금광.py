n, m = map(int,input().split())
arr = [[i for i in range(m)] for _ in range(n)]
temp =list(map(int,input().split()))
# 04
# 14
# 24까지 가야함 그러면 -> 0123/ 4567 / 891011
# -> (n)*4부터  (n+1)*4-1까지 
for i in range(n):
    print((i)*m,":",(i+1)*m)
    arr[i]= temp[(i)*m:(i+1)*m] 
print(arr)

for i in range(1,m):
    for j in range(n):
        print(arr[j][i])
        top,mid,bottom = 0,0,0
        if j != 0 :
            top = arr[j-1][i-1]
        if j != n-1:
            bottom = arr[j+1][i-1]
        mid = arr[j][i-1]
        arr[j][i] += max(top,mid,bottom)

result = 0

for i in range(n):
    result = max(result,arr[i][n-1])

print(result)
