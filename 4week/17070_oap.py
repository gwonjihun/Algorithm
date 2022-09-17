def maps(size : int):
    return [list(map(int,input().split())) for _ in range(0,size)]

def dfs(pos, graph, cnt,n):
    x,y,z = pos
    if x == n -1 and y == n-1:
        cnt += 1
        return 
    print(graph)

def action():
    cnt = 0
    sizes = int(input())
    graph = maps(size=sizes)
    cnt = dfs((0,1,0),graph,cnt,sizes)
    # map 2차원 배열로 입력 받는 부분
    print(graph)

    

if __name__=="__main__":
    action()