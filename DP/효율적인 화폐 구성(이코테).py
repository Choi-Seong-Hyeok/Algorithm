import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

dp = [sys.maxsize] * (m+1)
print(dp)
dp[0] = 0
for i in range(n):
    for j in range(arr[i],m+1):
        if dp[j - arr[i]] != sys.maxsize:
            dp[j] = min(dp[j-arr[i]]+1,dp[j])

print(dp[m])
