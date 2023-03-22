'''

1. 2차원 배열 입력 받기
2. dfs 함수 만들기
2-1. 매개변수 x,y를 받아 Out of Range면 pass
2-2. 상,하,좌,우 check
etc ..

'''
import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
graph = []

for _ in range(n):
    arr = list(map(int,input().rstrip()))
    graph.append(arr)

def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 상
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j)== True:
            result += 1
print(result)
