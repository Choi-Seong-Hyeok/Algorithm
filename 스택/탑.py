import sys

n = int(sys.stdin.readline())
heights = list(map(int, sys.stdin.readline().split()))
stack = []

for i in range(n):
    while stack:
        if stack[-1][1] > heights[i]:
            print(stack[-1][0], end=' ')
            break
        stack.pop()
    else:
        print(0, end=' ')
    stack.append((i+1, heights[i]))
