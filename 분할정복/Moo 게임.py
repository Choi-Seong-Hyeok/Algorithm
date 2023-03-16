import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

n = int(input())
k = 3
moo = "moo"
idx = 0
def oPlus(k):
    result = 'm' + ('o' * (k+2))
    return result

def mooRecur(n,k):
    if n == 0:
        return moo
    else:
        x = mooRecur(n-1,k)
        y = oPlus(n)
        return x + y + x
target = mooRecur(n,k)
print(target[n-1])