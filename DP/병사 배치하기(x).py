import sys
input = sys.stdin.readline

n = int(input())

combat_power = list(map(int,input().rstrip().split()))

dp = [0] * n

for i in range(1,n-1):
    if combat_power[i] > combat_power[i-1]:
        dp[i] = 1
    else:
        dp[i] = dp[i-1]

print(dp)
print(dp[n-1])