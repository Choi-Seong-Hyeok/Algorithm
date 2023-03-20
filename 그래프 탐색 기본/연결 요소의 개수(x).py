import sys

input = sys.stdin.readline

'''
방문 체크 리스트 필요.
2차원 리스트로 값 받는거 필요
해당 노드에 도착했을때 깊숙히 파고드는 것 필요.
하나하나씩 넣는 것 필요 ..? 
'''

# dfs로 그래프를 탐색한다.
def dfs(start):

    # 해당 노드를 방문체크 한다.
    visited[start] = True

    # 해당 시작점을 기준으로 계속해서 dfs로 그래프탐색한다.
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

N,M = map(int, input().split())
graph = [ [] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (1+N)
count = 0 # 컴포넌트 그래프 개수 저장

# 1 ~ N번 노드를 각각 돌면서
for i in range(1, N+1):
    
    if not visited[i]:
        if not graph[i]:
            count+=1
            visited[i] = True
        else:
            dfs(i)
            count += 1

print(count)