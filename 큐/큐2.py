import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
dq = deque()

def q_push(n):
    return dq.append(n)

def q_pop():
    if not dq:
        print(-1)
        return
    else:
        print(dq[0])
        dq.popleft()
        return

def q_size():
    print(len(dq))
    return

def q_empty():
    if not dq:
        print(1)
        return
    else:
        print(0)
        return
def q_front():
    if dq:
        print(dq[0])
        return
    else:
        print(-1)
        return
def q_back():
    if dq:
        print(dq[-1])
        return
    else:
        print(-1)
        return




for i in range(n):
    q_input =list(map(str, sys.stdin.readline().split()))
    if q_input[0] =='push':
        q_push(int(q_input[1]))
    elif q_input[0] == 'pop':
           q_pop()
    elif q_input[0] == 'size':
        q_size()
    elif q_input[0] == 'empty':
        q_empty()
    elif q_input[0] == 'front':
        q_front()
    elif q_input[0] == 'back':
        q_back()
    else:
        print(-1)



