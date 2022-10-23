n, k = map(int,input().split())

lan = [ int(input()) for _ in range(n) ]

start , end = 1, max(lan)

while start<= end:
    mid = (start+end)//2

    result = 0
    for i in lan:
        result += i//mid

    if result >= k:
        start = mid+1
    else :
        end = mid-1

print(end)