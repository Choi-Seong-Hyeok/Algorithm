N,M = map(int,input().split())
iceList = []

# 입력
for _ in range(N):
    ice = list(map(int,input()))
    iceList.append(ice)

def dfs(x,y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    if iceList[x][y] == 0:
        iceList[x][y] = 1
        dfs(x-1,y) # 하
        dfs(x+1,y) # 상
        dfs(x,y-1) # 좌
        dfs(x,y+1) # 우
        return True
    return False
cnt = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            cnt += 1

print(cnt)