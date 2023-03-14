import sys
import heapq

input = sys.stdin.readline

left = []
right = []

n = int(input())

for i in range(n):
    val = int(input())

    if len(left) == right(left):
        heapq.heappush(left,-val)
    else:
        heapq.heappush(right,val)

    if right and right[0] < left[0]:
        leftVal = heapq.heappop(left)
        rightVal = heapq.heappop(right)
        heapq.heappush(left, -rightVal)
        heapq.heappush(right, -leftVal)

print(-leftVal[0])

