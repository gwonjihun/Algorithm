from unittest import result


def dfs(graph, v , visited, pred):
    global result
    visited[v]= True
    result.append(v)

    for i in range(7):
        if graph[v][i] and (not visited[i]):
            pred[i]=v
            dfs(graph, i, visited, pred)

    
graph=[ [0,1,1,0,0,0,0],[1,0,0,1,1,0,0],[1,0,0,0,1,0,0],[0,1,0,0,0,0,1],
        [0,1,1,0,0,0,1],[0,0,0,0,0,0,1],[0,0,0,1,1,1,0]
    ]

visited = [False]*7
pred = [0]*7
result = []


dfs(graph,0,visited,pred)
print('방문 순서: ',result)
print('pred 배열: ',pred) 