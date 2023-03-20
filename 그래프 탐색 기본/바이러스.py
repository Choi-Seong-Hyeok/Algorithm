import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

virus = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().rstrip().split())
    virus[a].append(b)
    virus[b].append(a)

visited_virus = [False] * (n+1)
count = 0
def dfs(v):
    global count
    visited_virus[v] = True
    for i in virus[v]:
        if not visited_virus[i]:
            dfs(i)
            count += 1

        


for i in range(1,n):
    if visited_virus[i] == False:
        dfs(i)
        break
        

print(count)
