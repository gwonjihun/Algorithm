n, m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

print(max( min(i) for i in arr ))