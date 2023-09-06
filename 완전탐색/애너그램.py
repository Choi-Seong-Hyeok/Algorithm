from itertools import permutations
import sys
'''
    abc
    [F,F,F]
    acba

'''
N = int(input())
alphaList = []
visited = []
for _ in range(N):
    alpha = str(sys.stdin.readline().rstrip())
    alphaList.append(alpha)
for i in range(len(alphaList)):
    val = [False] * len(alphaList[i])
    visited.append(val)
result = []

def dfs(depth,start,visited):
    if depth == len(visited):


    else:
        for i in range(start,len(visited)):
            if visited[i] == False:
                visited[i] = True
                dfs(depth +1 ,i,visited)
                visited[i] = False






for i in visited:
    dfs(0,0,i)
