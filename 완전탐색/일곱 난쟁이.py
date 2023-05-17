import sys
input = sys.stdin.readline

# 이중 for문으로 두 값들을 계속 더해가 값 찾으면 반복문 break
nan = []

temp1,temp2 = 0,0

for _ in range(9):
    a = int(input())
    nan.append(a)

val = sum(nan) - 100

for i in range(len(nan)):
    for j in range(i+1,len(nan)):
        res = nan[i] + nan[j]
        if res == val:
            temp1 = nan[i]
            temp2 = nan[j]


nan.remove(temp1)
nan.remove(temp2)
nan.sort()

for i in range(len(nan)):
    print(nan[i])




