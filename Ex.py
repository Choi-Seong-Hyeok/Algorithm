import sys
input = sys.stdin.readline
N, M, V = map(int,input().rstrip().split())

'''
dfs시 노드를 방문했는지 알기위한 리스트 필요 O
각 노드의 위치를 나타낼 수 있는 배열 or 인접리스트 필요 O [2차원 배열]
'''

graph = [[False] * (N+1) for _ in range(N+1)]
visited_dfs = [False] * (N+1)
for _ in range(N+1):
    a,b = map(int,input().rstrip().split())
    graph[a][b] = True
    graph[b][a] = True

def dfs(V):
    '''
    1) Visited Check
    2) 깊이 들어가야함.
    '''
    visited_dfs[V] = True
    print(V,end=" ")
    for i in range(1,N+1):
        if not visited_dfs[i] and graph[V][i]:
            dfs(i)


dfs(V)
print()

