'''
0 0 0 0 0 
1 0 0 0 0
1 1 0 0 0
1 1 1 0 0
1 1 0 1 0
1 1 0 0 1 
... 
1.재귀
1-1. 재귀 종료조건 depth
1-2. 합이 100이면 종료
2. 방문 했는지 visit배열
'''

short_men = [int(input()) for _ in range(9)]
visited = [0,0,0,0,0,0,0,0,0]

def dfs(start,depth):
    if depth == 7:
        resultList = []
        for i in range(len(visited)):
            if visited[i] == 1:
                resultList.append(short_men[i])
        if sum(resultList) == 100:
            for i in sorted(resultList):
                print(i)
            exit()
        else:
            return
    else:
        for i in range(start,len(visited)):
            if visited[i] == 0:
                visited[i] = 1
                dfs(i+1,depth + 1)
                visited[i] = 0


dfs(0,0)

