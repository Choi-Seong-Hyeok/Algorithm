def dfs(g,s,v):
    v[s] = True
    print(s,' ')
    for i in g[s]:
        if v[i] == False:
            v[i] = True
            dfs(g,i,v)



graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9
dfs(graph,1,visited)

