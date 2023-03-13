import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
Josephus = deque()
result = []
for i in range(1, n+1):
    Josephus.append(i)

while 1:
    for i in range(k):
        if i == k-1:
            result.append(Josephus.popleft())
            break
        Josephus.append(Josephus.popleft())
    if not Josephus:
        break

print('<' + str(result)[1:-1] + '>' )