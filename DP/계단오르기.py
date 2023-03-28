import sys
input = sys.stdin.readline
'''
max(n-1 까지 최대값,n-2 까지 최대값) 
'''
n = int(input())
dp = [0] * n
stairs = []

for _ in range(n):
    val = int(input())
    stairs.append(val)

dp[0] = stairs[0]
dp[1] = stairs[1] + stairs[0]
dp[2] = max(stairs[0]+stairs[2],stairs[1]+stairs[2])

for i in range(3,n):
    dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i],dp[i-2]+stairs[i])
print(dp[n-1])