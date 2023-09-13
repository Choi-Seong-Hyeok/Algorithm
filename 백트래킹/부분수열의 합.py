from itertools import combinations

N,S = map(int,input().split())
NList = list(map(int,input().split()))
cnt = 0

for i in (range(1,N+1)):
    val = combinations(NList,i)
    for i in val:
        result = sum(list(i))
        if result == S:
            cnt += 1
print(cnt)

