'''
 9개의 숫자 중 7개를 더해 합이 100이되도록
'''
from itertools import permutations
totalList = []
result = []
for _ in range(9):
    val = int(input())
    totalList.append(val)


for i in permutations(totalList,7):
    result = list(i)
    if sum(i) == 100:
        result = i
        break
result = sorted(result)
for i in result:
    print(i)