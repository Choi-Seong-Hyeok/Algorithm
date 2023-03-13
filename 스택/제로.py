import sys
from collections import deque

k = int(sys.stdin.readline())

dq = deque()
for i in range(k):
    val = int(sys.stdin.readline())
    if val == 0:
        dq.pop()
    else:
        dq.append(val)

print(sum(dq))
