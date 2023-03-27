import sys
input = sys.stdin.readline

'''
target = dp[k+1][w]
2차원 배열에 입력

'''
w,k = map(int,input().rstrip().split())
backpack = [[0,0]]
dp = [[0 for _ in range(k+1)] for _ in range(w)]


for _ in range(w):
    a = list(map(int,input().rstrip().split()))
    backpack.append(a)


for i in range(1, k+1):
    nw, nv = backpack[i][0], backpack[i][1]
    for j in range(1, k+1):
        if j >= nw :
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-nw] + nv)
        else :
            dp[i][j] = dp[i-1][j]
print(dp[-1][-1])















