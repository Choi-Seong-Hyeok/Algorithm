import sys
input = sys.stdin.readline

T = int(input())

while 0 < T:
    n = int(input())
    coin = list(map(int,input().spit()))
    target = int(input())

    coins = [0 for _ in range(target + 1)]
    coins[0] = 1
    for i in range(n):
        # 그 값부터 끝까지
        for j in range(coin[i],target + 1):
            coins[j] += coins[j-coin[i]]

    print(coins[target])
    T -= 1




