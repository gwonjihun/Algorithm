
n = int(input())
arr = [list(map(int,input().split( ))) for _ in range(0,n)]
result = []

# 1. n이 1이 되면 
# x: 배열의 x 시작 위치
# y: 배열의 y 시작 위치
# n: x+n,y+n으로 배열의 마지막 위치 찾아주기
def binary_search(x,y,n):
    color = arr[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != arr[i][j]:
                binary_search(x,y,n//2)
                binary_search(x,y+n//2,n//2)
                binary_search(x+n//2,y,n//2)
                binary_search(x+n//2,y+n//2,n//2)   
                return
    if color == 0:
        result.append(0)
    elif color == 1:
        result.append(1)

binary_search(0,0,n)
print(result.count(0))
print(result.count(1))