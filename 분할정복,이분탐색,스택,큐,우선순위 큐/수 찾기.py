import sys


N = int(input())
NList = set(map(int,input().split()))

M = int(input())
MList = list(map(int,input().split()))

for ML in MList:
    if ML in NList:
        print(1)
    else:
        print(0)

