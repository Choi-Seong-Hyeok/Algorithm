import sys
input = sys.stdin.readline

x = str(input())
y = str(input())
dp = [[0 for i in range(len(y))] for i in range(len(x))]


for i in range(1,len(x)):
    for j in range(1,len(y)):
        if x[i-1] == y[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(dp[len(x)-1][len(y)-1])

