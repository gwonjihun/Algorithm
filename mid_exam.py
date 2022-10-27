# from collections import deque

# N, M = map(int,input().split())

# arr = []
# visited = [False * M]
# for _ in range(M):
#     x, y = map(int,input().split())
#     arr.append((x,y))
# mid, end = map(int,input().split())
# #  완전 탐색 알고리즘으로 해결한다면?
# #  ex
# start = 1
# result = []
# print(arr)

# def dfs(graph,v,visited,pred):
#     global result
#     visited[v] = True
#     result.append(v)
#     for i in range(