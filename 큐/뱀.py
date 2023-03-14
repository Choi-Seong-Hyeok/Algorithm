import sys
from collections import deque

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

snakeGraph = [[0] * n for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for i in range(k):
    a, b = map(int,sys.stdin.readline().split())
    snakeGraph[a - 1][b - 1] = 2

i = int(sys.stdin.readline())
dirDict = dict()
dq = deque()
dq.append((0, 0))

for i in range(i):
    x, c = input().split()
    dirDict[int(x)] = c

x,y = 0
snakeGraph[x][y] = 1
cnt = 0
direction = 0


def turn(alpha):
    global direction
    if alpha == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4


while 1:
    cnt += 1
    x += dx[direction]
    y += dy[direction]

    if x < 0 or x >= n or y < 0 or y >= n:
        break

    if snakeGraph[x][y] == 2:
        snakeGraph[x][y] = 1
        dq.append((x,y))
        if cnt in dirDict:
            turn(dirDict[cnt])
        elif snakeGraph[x][y] == 0:
            snakeGraph[x][y] = 1
            dq.append((x,y))
