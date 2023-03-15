import sys
input = sys.stdin.readline

def fibo(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)






N = int(input())
print(fibo(N))