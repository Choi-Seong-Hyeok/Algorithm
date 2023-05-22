import sys
input = sys.stdin.readline
answer = 0

k = int(input())
dungeons = []

def dfs(k,cnt,dungeons,visited):
    global answer
    if cnt > answer:
        answer = cnt
    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            dfs(k - dungeons[i][1],cnt+1,dungeons,visited)
            visited[i] = False



for i in range(3):
    dungeons.append(list(map(int,input().split())))


visited = [False] * len(dungeons)

dfs(k,0,dungeons,visited)

print(answer)



