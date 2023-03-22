import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

T = int(input())

idx = 0
while idx<T:
        m,n,k = map(int,input().rstrip().split())
        
        cabbage_list = [[0]*(n) for _ in range(m)]
        
        for _ in range(k):
            a,b = map(int,input().rstrip().split())
            cabbage_list[a][b] = 1

        def dfs(x,y):
            if x <= -1 or x >= m or y >= n or y <= -1:
                return False
            if cabbage_list[x][y] == 1:
                cabbage_list[x][y] = 0
                # 상
                dfs(x-1,y)
                # 하
                dfs(x+1,y)
                # 우
                dfs(x,y+1)
                # 좌
                dfs(x,y-1)
                return True
            return False
        result = 0
        for i in range(m):
            for j in range(n):
                if dfs(i,j) == True:
                    result += 1
        print(result)
        idx += 1