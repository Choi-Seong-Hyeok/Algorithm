import sys
from bisect import bisect_left,bisect_right


N,x = map(int,sys.stdin.readline().split())
array = list(map(int,sys.stdin.readline().split()))



def find_x(a,y):
    left = bisect_left(a,y)
    right = bisect_right(a,y)
    result = right - left
    if result != 0:
        print(result)
    else:
        print(-1)


find_x(array,x)