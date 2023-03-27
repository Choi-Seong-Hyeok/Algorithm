import sys
input = sys.stdin.readline

n,k = map(int,input().rstrip().split())
coins = []
cnt = 0
for _ in range(n):
    a = int(input())
    coins.append(a)

coins.reverse()


for coin in coins:
    while coin <= k:
        if coin > k:
            break
        cnt += 1
        k -= coin

print(cnt)
