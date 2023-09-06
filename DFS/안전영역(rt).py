'''
 기준 값을 몇으로 둘것이냐 ?
 --> 배열의 최소값과 최대값사이에 모든 값들
'''
import sys
sys.setrecursionlimit(100000)

rainList = [] # 기준 장마 리스트
resultList = [] # 각 영역마다 리스트 
maxs = 0
mins = float('inf')
N = int(input())

for i in range(N):
    val = list(map(int,input().split()))

    if maxs > max(val):
        pass
    elif max(val) > maxs:
        maxs = max(val)
    if mins < min(val):
        pass
    elif mins > min(val):
        mins = min(val)
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
min = 0
for _ in range(N):
     val = [0] * N
     visited.append(val)

i = 0
while(i <= maxs):
    cnt = 0
    for i in range(N): # 방문 리스트 작성
         for j in range(N):
              if rainList[i][j] > mins:
                   visited[i][j] = True
              else:
                   visited[i][j] = False

    for i in range(N):
        for j in range(N):
            if rainList[i][j] > mins:
                if dfs(i,j,mins,visited) == True:
                        cnt += 1

    resultList.append(cnt)
    i += 1

print(max(resultList))

     

        


