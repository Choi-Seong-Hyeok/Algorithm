import sys


def fibo(val):
    if val <= 1:
        return 1
    else:
        return fibo(val-1) + fibo(val-2)



n = int(input())
print(fibo(n))
