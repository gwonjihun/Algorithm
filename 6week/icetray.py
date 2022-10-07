def split_arr(s):
    result = [ int(i) for i in s]
    return result
a,b = map(int,input().split())


arr = [ split_arr(input()) for _ in range(a)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
answer = 0
def dfs(x,y):
    global arr
    if x<0 or x>=a or y<0 or y >=b:
        return False
    if arr[x][y] == 0:
        arr[x][y] = 1
        print(arr)
        for i in range(0,4):
            dfs(x+dx[i],y+dy[i])
        return True
    return False


for i in range(a):
    for j in range(b):
        if dfs(i,j)==True:
            answer+=1
print(answer)