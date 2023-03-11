import sys

# K개의 랜선과 필요로하는 랜선의 개수 N
K,N = map(int,sys.stdin.readline().split())

LANCable = []
for i in range(K):
    val = int(sys.stdin.readline())
    LANCable.append(val)

LANCable.sort()

start = 0
end = max(LANCable)
result = 0
while start <= end:

    mid = (start + end)//2
    cnt = 0

    for lan in LANCable:
        if lan >= mid:
            cnt += lan // mid
    if cnt >= N:
        start = mid + 1
    else:
        # result = mid
        end = mid - 1


print(end)
