import sys
input = sys.stdin.readline

n = int(input())
food_storage = list(map(int,input().rstrip().split()))

dp = [0] * len(food_storage)

dp[0] = food_storage[0]
dp[1] = max(food_storage[0],food_storage[1])
for i in range(2,n):
    dp[i] = max(dp[i-1],dp[i-2] + food_storage[i])


print(dp[n-1])