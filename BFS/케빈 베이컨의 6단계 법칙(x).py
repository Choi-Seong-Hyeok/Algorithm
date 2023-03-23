import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().rstrip().split())
    graph[a].append(b)

def bfs(start,dst,visited):
    arr = []
    queue = deque([start])
    dst[start] = 0
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(v)
                distance[i] = distance[v] + 1
                arr.append(distance[i])
                visited[i] = True
   




result_list = []
for i in range(1,n):
    distance = [0] * (n+1)
    visited = [False] * (n+1)
    a=bfs(i,distance,visited)
    result_list.append(a)
print(result_list)
