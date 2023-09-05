import sys
sys.setrecursionlimit(10**5)

N,M = map(int,input().split())

graph = [[]for _ in range(N+1)]
cnt = 0

for _ in range(M):
    a,b = map(int,input().split())
    graph[b].append(a)
    graph[a].append(b)


visited = [False] * (N+1)

def dfs(visited,start,graph):
    global cnt
    visited[start] = True
    for i in graph[start]:
         if visited[i] == False:
            dfs(visited,i,graph)

        

for i in range(1,N+1):
   if not visited[i]:
        dfs(visited,i,graph)
        cnt += 1


print(cnt)



