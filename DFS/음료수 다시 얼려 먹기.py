
N,M = map(int,input().split())
iceList = []
cnt = 0 # 얼음의 개수
for _ in range(N):
    val = list(map(int,input()))
    iceList.append(val)

def dfs(x,y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if iceList[x][y] == 0:
        iceList[x][y] = 1
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False




for i in range(N):
    for j in range(M):
        if iceList[i][j] == 0:
            if dfs(i,j) == True:
                cnt += 1
print(cnt)




# dfs()
# print(cnt)