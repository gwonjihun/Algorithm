import math,sys
input = sys.stdin.readline

n,c = map(int,input().split())
home = [int(input()) for _ in range(n)]
home.sort()
start, end = 1, home[n-1]-home[0]

result = 0

if c ==2:
    print(home[n-1]-home[0])
else:
    while(start< end):
        mid = (start+end)//2

        count = 1
        ts = home[0]
        for i in range(n):
            if home[i] - ts >= mid :
                count += 1
                ts = home[i]
        if count >= c:
            result = mid
            start = mid +1
        elif count <c :
            end = mid
print(result)