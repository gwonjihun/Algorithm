n = int(input())

arr = [ [ list(map(int,input().split()))] for _ in range(n)]
#  9개로 자른다는 뜻은 결국 x와 y를 3으로 나눈다


result_minus = 0
result_zero = 0
result_one = 0

def dfs(x,y,n):
    
    num