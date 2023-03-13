import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
dq = deque()
for i in range(1, n+1):
    dq.append(i)
try:
    while 1:
            dq.popleft()
            dq.append(dq.popleft())
            if len(dq) == 1:
                break

    print(dq.popleft())
except IndexError:
    print(n)