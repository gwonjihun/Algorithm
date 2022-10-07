# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, u , v):
    u = find_parent(parent,u)
    v = find_parent(parent,v)
    if u < v :
        parent[v] = u
    else:
        parent[u] = v

n,m = map(int,input().split())