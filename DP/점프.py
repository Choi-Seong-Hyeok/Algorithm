try:
    n, k = map(int, input().split())  # 돌의 개수 n과 최대 점프 거리 k를 입력 받습니다.
    stones = [False] * (n+1)  # 돌이 있는 위치를 저장할 리스트를 생성합니다.
    for i in range(n):
        stones[int(input())] = True  # 돌이 있는 위치를 입력 받아 해당 위치를 True로 설정합니다.
except EOFError:
        pass  # 입력이 더 이상 없는 경우 무시합니다.



dp = [float('inf')] * (n+1)  # 각 위치에서의 최소 점프 횟수를 저장할 리스트를 생성합니다.
dp[1] = 0  # 시작 위치에서의 점프 횟수는 0입니다.

for i in range(1, n+1):
    if not stones[i]:  # 현재 위치에 돌이 없는 경우
        for j in range(1, k+1):  # 가능한 모든 점프 거리에 대해
            if i+j > n:  # 범위를 벗어나는 경우 건너뜁니다.
                continue
            dp[i+j] = min(dp[i+j], dp[i]+1)  # 해당 거리로 이동하는 최소 점프 횟수를 갱신합니다.
    else:  # 현재 위치에 돌이 있는 경우
        for j in range(1, k+1):  # 가능한 모든 점프 거리에 대해
            if i+j > n:  # 범위를 벗어나는 경우 건너뜁니다.
                continue
            if not stones[i+j]:  # 해당 거리로 이동할 수 있는 경우
                dp[i+j] = min(dp[i+j], dp[i]+1)  # 해당 거리로 이동하는 최소 점프 횟수를 갱신합니다.

if dp[n] == float('inf'):  # n 위치에 도달할 수 없는 경우
    print("-1")
else:  # n 위치에 도달할 수 있는 경우
    print(dp[n])
