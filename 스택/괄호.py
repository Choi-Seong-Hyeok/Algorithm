import sys
from collections import deque
t = int(sys.stdin.readline())

for i in range(t):
    dq = deque()
    data = list((input()))
    for d in data:
        if not dq:
            dq.append(d)
        else:
            if d == ')':
                if dq[-1] == '(':
                    dq.pop()
                else:
                    dq.append(d)
            else:
                dq.append(d)
    if not dq:
        print('YES')
    else:
        print('NO')


