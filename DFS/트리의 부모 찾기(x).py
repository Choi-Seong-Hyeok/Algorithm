'''
    1. visited 배열
    2. parent 배열
    3. dfs돌때 parent배열에 check node 올림.
'''
import sys
input = sys.stdin.readline

def dfs(node):
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            parent[i] = node
            dfs(i)



    


n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
parent = [False] * (n+1)

for _ in range(n-1):
    a,b = map(int,input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)

for i in range(2,len(parent)):
    print(parent[i])

























