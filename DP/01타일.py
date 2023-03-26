import sys
input = sys.stdin.readline


def tile(n):
    t = [1,2]
    for i in range(2,n+1):
        t.append((t[i-1] + t[i-2])%15746)

    return t[n-1]




n = int(input())

print(tile(n))