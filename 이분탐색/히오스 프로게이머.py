import sys

N, K = map(int, sys.stdin.readline().split())

levels = []

for i in range(N):
    levels.append(int(sys.stdin.readline()))

start, end = min(levels), min(levels) + K
result = 0
while start <= end:
    mid = (start + end)//2
    cnt = 0
    for level in levels:
        if level < mid:
            cnt += (mid - level)

    if cnt <= K:
        start = mid + 1
        result = max(mid, result)
    else:

        end = mid - 1

print(result)



