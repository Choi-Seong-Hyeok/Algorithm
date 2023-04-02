import sys
input = sys.stdin.readline

n = int(input())



stairs = []

dp = [0] * (n+1)

for _ in range(n):
    a = int(input())
    stairs.append(a)


dp[0] = 0
dp[1] = stairs[0]
dp[2] = stairs[0]+stairs[1]

for i in range(3,n+1):
    dp[i] = max(dp[i-3]+stairs[i-2]+stairs[i-1],dp[i-2]+stairs[i-1])

print(dp[n])