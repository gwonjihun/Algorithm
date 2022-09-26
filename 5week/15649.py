n,m = map(int,input().split())

results = []

def dfs():
    if len(results)==m:
        print(' '.join(map(str,results)))
        return

    for i in range(1,n+1):
        #print(results)
        if i not in results:
            results.append(i)
            dfs()
            results.pop()

dfs()