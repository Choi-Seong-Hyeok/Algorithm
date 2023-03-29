import sys 
input = sys.stdin.readline

# 입력 받은 수 
n = int(input())

dp = [0] * (n+1)

for i in range(2,n+1):
    # 현재 계산하고자 하는 값의 전 값의 "횟수" + 1(+1은 뺴기 1을 했으니)
    dp[i] = dp[i-1] + 1
    # i가 3으로 나누어 떨어질때..
    if i % 3 == 0:
        # 3으로 나눈 그 수에다가 + 1(내가 나누려고 진행했으니 횟수를 구하는거잖아? 그러니 +1을 해줘야지)
        dp[i] = min(dp[i//3]+1,dp[i])
    if i % 2 == 0:
        dp[i] = min(dp[i//2]+1,dp[i])

print(dp[n-1])



