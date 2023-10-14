'''
    1            4
  2      3     5    6
7  8  9

'''

n = int(input())
number1,number2 = map(int,input().split())
m = int(input())
graph = [[]for _ in range(n+1)]
visited = [False]*(n+1)
print(visited)

for _ in range(m):
    parent,child = map(int,input().split())
    graph[child].append(parent)
    graph[parent].append(child)

cnt = 0

def dfs(x,y,result):
    global cnt
    if graph[x][y] == result:
        return
    for i in range(x,n+1):
        if visited[i] == False:
            visited[i] = True
            dfs(i+1)


dfs(number1,0,number2)



