N = int(input())

network = int(input())
computer = []
cnt = 0
for _ in range(N+1):
    a = []
    computer.append(a)

for _ in range(network): # 간선을 연결해주는 
    first,second = map(int,input().split())
    computer[first].append(second)
    computer[second].append(first)

visited = [False] * (N+1) # 방문했는지 여부 배열 

def dfs(start,visited):
    global cnt
    visited[start] = True
    for i in computer[start]:
        if not visited[i]:
            cnt += 1
            dfs(i,visited)




dfs(1,visited)
print(cnt)