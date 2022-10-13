from itertools import combinations
from math import inf

n,m = map(int,input().split())

town = [list(map(int,input().split())) for _ in range(n)]

# 1. 입력에서 1,2이 x,y값 따로 저장해놓는다
# 2. 전체에서 치킨 가게 m개만 선택한다
# 3. 선택 후 치킨거리를 저장한다.
# 4. global answer값과 비교하여 최소 값만 저장한다.
# 
# 3. 
house = []
chiken = []
for i in range(n):
    for j in range(n):
        if town[i][j] == 1: house.append((i,j))
        elif town[i][j] == 2: chiken.append((i,j))

minload = 1e9
for ch in combinations(chiken,m):
    sumv = 0
    for home in house:
        sumv += min([abs(home[0]-i[0])+abs(home[1]-i[1]) for i in ch])
    minload = min(sumv,minload)       

print(minload)