N = int(input())

network = int(input())
computer = []
cnt = 0
for _ in range(network+1):
    a = []
    computer.append(a)

for _ in range(network):
    first,second = map(int,input().split())
    computer[first].append(second)

visited = [False] * (network+1)

def dfs(start,visited):
    global cnt
    visited[start] = True
    for i in computer[start]:
        if not visited[i]:
            cnt += 1
            dfs(i,visited)
    



dfs(1,visited)
print(cnt)