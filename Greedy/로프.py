# 2(k)개의 로프를 사용하여 중량이 20(w)인 물체를 들어 올릴때
# 각각의 로프에는 모두 고르게 10(w/k)만큼의 중량이 걸리게된다.
# 최대 w를 구하는게 문제의 의도.
# k는 나와있고
# w인 물체..
# X // 2 = w 여기서 w를 구해야함 -> w를 구하려면 X를 구해야함
# w가 20이라고 가정할때, 10씩 중량 가능..?
# 1) 10 
# 2) 15

# Case 1) 최대 중량 중 최소 중량에 기준 맞추기
# minRope = min(ropeList)
# print(2*minRope)
# Case 2) 임의로 몇 개의 로프를 골라서 사용

import sys

k = int(input())
ropeList = [int(sys.stdin.readline().rstrip()) for i in range(k)]
compareRope = []

ropeList.sort(reverse=True)

for i in range(k):
    compareRope.append(ropeList[i] * (i+1))


print(max(compareRope))