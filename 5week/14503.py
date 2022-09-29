from re import L


wid, hi = map(int,input().split())

state = list(map(int,input().split()))

arr = [[0]*hi]*wid

for i in range(wid):
    arr[i] = list(map(int,input().split()))
# 0이면 위 1 은 오른쪽 2는 아래 3은 왼쪽
print(state)
print(arr[state[0]-1][state[1]-2])