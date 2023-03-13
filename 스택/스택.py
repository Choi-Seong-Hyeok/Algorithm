import sys


n = int(sys.stdin.readline())
stx = []

def stx_push(list_stx, val):
    list_stx.append(val)
    return

def stx_pop(list_stx):
    if not list_stx:
        print(-1)
        return
    else:
        print(list_stx[-1])
        del list_stx[-1]
        return

def stx_top(list_stx):
    if not list_stx:
        print(-1)
        return
    else:
        print(list_stx[-1])
        return

def stx_size(list_stx):
    print(len(list_stx))
    return

def stx_empty(list_stx):
    if not list_stx:
        print(1)
        return
    else:
        print(0)
        return




for i in range(n):
    put = list(sys.stdin.readline().split())
    if put[0] == 'push':
        stx_push(stx, int(put[1]))
    else:
        if put[0] == 'pop':
            stx_pop(stx)
        elif put[0] == 'top':
            stx_top(stx)
        elif put[0] == 'size':
            stx_size(stx)
        elif put[0] == 'empty':
            stx_empty(stx)
        else:
            break



