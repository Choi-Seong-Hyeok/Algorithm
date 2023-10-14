N, M = map(int, input().split())

graph = [[]for _ in range(N+1)]

for _ in range(M):
    a,b = map(int, input().split())
    graph[b].append(a)
    graph[a].append(b)

visited = [False] * (N+1)

def dfs(i):
    # 방문처리
    visited[i] = True
    for i in graph[i]:
        if visited[i] == False:
            visited[i] = True

cnt = 0

for i in range(N):
    if visited[i] == False:
        dfs(i)
        cnt += 1

print(cnt)




