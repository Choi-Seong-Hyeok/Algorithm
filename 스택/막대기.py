import sys
from collections import deque
n = int(sys.stdin.readline())
stack = []
cnt = 1
for i in range(n):
    h = int(sys.stdin.readline())
    stack.append(h)

top_bar = stack[-1]

for i in range(n-2,-1,-1):
    if stack[i] > top_bar:
        cnt += 1
        top_bar = stack[i]


print(cnt)