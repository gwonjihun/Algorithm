import mimetypes


n = int(input())
arr = list(map(int,input().split()))
add, mi, mu, did = map(int,input().split())
maxnum = -1e9
minimum= 1e9
def dfs(depth, total, plus, minus, multiply,divide):
    global maxnum,minimum
    if depth==n:
        maxnum=max(total,maxnum)
        minimum=min(total,minimum)
        return

    if plus:
        dfs(depth+1,total+arr[depth],plus-1,minus,multiply,divide)
    if minus:
        dfs(depth+1,total-arr[depth],plus,minus-1,multiply,divide)
    if multiply:
        dfs(depth+1,total*arr[depth],plus,minus,multiply-1,divide)
    if divide:
        dfs(depth+1,int(total/arr[depth]),plus,minus,multiply,divide-1)

dfs(1,arr[0],add,mi,mu,did)
print(maxnum)
print(minimum)        