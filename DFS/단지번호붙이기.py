import sys
input = sys.stdin.readline

n = int(input().rstrip())
graph = [list(map(int,input().rstrip())) for _ in range(n)]
curr_time = 0

def dfs(x,y):
    global curr_time
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        curr_time += 1
        graph[x][y] = 0
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False





result = 0
time_list = []
for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            time_list.append(curr_time)
            result += 1
            curr_time = 0
time_list.sort()
print(result)
for i in time_list:
    print(i)
