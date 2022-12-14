def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

n,m = map(int, input().split())

parent = [0] * (n)
for i in range(0,n):
    parent[i] = i

arrs = []
result = 0

for i in range(m):
    x,y,cost = map(int, input().split())
    arrs.append((cost,x,y))
    result += cost

arrs.sort()

for arr in arrs:
    cost,a,b = arr
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result -= cost

print(result)