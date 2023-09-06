'''
 기준 값을 몇으로 둘것이냐 ?
 --> 배열의 최소값과 최대값사이에 모든 값들(X)
 --> 0부터 최대값 사이에 모든 값들(O)
'''

import sys
sys.setrecursionlimit(100000)

rainList = [] # 기준 장마 리스트
resultList = [] # 각 영역마다 리스트 
maxs = 0 # 장마 리스트 안의 최대값
N = int(input())

for i in range(N):
    val = list(map(int,input().split()))

    if max(val) > maxs:
        maxs = max(val)
    rainList.append(val)


def dfs(x,y,mins,visited):
    if x <= -1 or x >= N or y >= N or y <= -1:
        return False
    if rainList[x][y] > mins and visited[x][y] == True:
            visited[x][y] = False
            dfs(x+1,y,mins,visited)
            dfs(x-1,y,mins,visited)
            dfs(x,y+1,mins,visited)
            dfs(x,y-1,mins,visited)
            return True
    return False

visited = []
for _ in range(N): # 방문 리스트 초기화
     val = [0] * N
     visited.append(val)

small = 1 # 1부터 max까지 모든 경우의 수를 구함
while(small < maxs):
    cnt = 0
    for i in range(N): # 방문 리스트 작성
         for j in range(N):
              if rainList[i][j] > small:
                   visited[i][j] = True
              else:
                   visited[i][j] = False

    for i in range(N):
        for j in range(N):
            if rainList[i][j] > small:
                if dfs(i,j,small,visited) == True:
                        cnt += 1

    resultList.append(cnt)
    small += 1

if resultList:
    print(max(resultList))
else:
    print(1)

