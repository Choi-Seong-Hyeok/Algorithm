import sys
input = sys.stdin.readline

n = int(input())

def move(start,end):
    print(start,end)

def hanoi(N,start,to,via):
    if N == 1:
        move(start,to)
    else:
        hanoi(N-1,start,via,to)
        move(start,to)
        hanoi(N-1,via,to,start)



hanoi(n,1,3,2)