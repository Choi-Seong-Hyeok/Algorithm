'''
1) N - 1
2) N // K
'''
import sys
input = sys.stdin.readline

n,k = map(int,input().rstrip().split())
cnt = 0

while 1:
    if n % k == 0:
        n //= k
        cnt += 1
    else:
        n -=1
        cnt += 1
    if n == 1:
        break


print(cnt)