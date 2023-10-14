'''
1. 그래프 나타내기
2. 방문 배열 나타내기
3. 재귀로 방문 배열을 활용하여 모든 노드들 탐색 함수 생성
'''

def dfs(g,i,v):
    v[i] = True
    print(i ,end = ' ')

    for i in g[i]:
        if not v[i]:
            dfs(g,i,v)

graph = [
    [], # index 1부터 나타내기위해 0은 비워둠
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9 # 방문 배열

dfs(graph,1,visited)