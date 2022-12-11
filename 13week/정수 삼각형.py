n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            up_left = 0
        else:
            up_left = arr[i-1][j-1]
        if j== i:
            up = 0
        else:
            up = arr[i-1][j]
        arr[i][j]= arr[i][j] + max(up,up_left)

print(max(arr[-1]))