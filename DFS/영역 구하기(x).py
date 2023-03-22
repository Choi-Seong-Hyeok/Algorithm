import sys
input = sys.stdin.readline

m,n,k = map(int,input().rstrip().split())
rectangle = [[0] * n for _ in range(m)]

for _ in range(k):
    x1,y1,x2,y2 = map(int,input().rstrip().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            rectangle[i][j] = 1
current_time = 0
def dfs(x,y):
    global current_time
    
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return 0
    if rectangle[x][y] == 1:
        return 0

    current_time += 1
    if rectangle[x][y] == 0:
        rectangle[x][y] = 1
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x,y+1)

    return current_time


current_list = []
for i in range(m):
    for j in range(n):
        if rectangle[i][j] == 0:
            current_time = 0
            cnt = dfs(i,j)
            current_list.append(cnt)

current_list.sort()
print(len(current_list))
for i in current_list:
    print(i, end = ' ')