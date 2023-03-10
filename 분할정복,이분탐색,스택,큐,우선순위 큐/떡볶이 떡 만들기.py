# 이코테 문제
import sys

n,m = map(int,sys.stdin.readline().split())
riceCakes = list(map(int,sys.stdin.readline().split(sep=' ',maxsplit=n)))

riceCakes.sort()

start,end = 0,max(riceCakes)

result = 0
while(start<=end):
    total = 0
    mid = (start+end)//2
    for riceCake in riceCakes:
        if riceCake > mid:
            total += riceCake - mid

    if total < m:
        end = mid -1
    else:
        result = mid
        start = mid + 1

print(result)