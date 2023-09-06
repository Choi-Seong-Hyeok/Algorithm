'''
1.철자 중복시 한 번만 출력
2.알파벳 순서대로
'''
from itertools import permutations
import sys

N = int(input())
alphaList = []
result = []
for _ in range(N):
    alpha = str(sys.stdin.readline().rstrip())
    alphaList.append(alpha)

for i in range(len(alphaList)):
    for j in permutations(alphaList[i],len(alphaList[i])):
        st = ''.join(j)
        if st not in result:
            result.append(st)
    arr = sorted(list(result))
    result = []
    answer = ""
    for i in arr:
        answer += str(i)+'\n'
    print(answer)
    




