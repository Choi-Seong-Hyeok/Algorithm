# 커피를 몇 번째 받는지에 따라 팁을 다른 액수로 줌
# W = X(원래 두려고 생각했던 돈) - (받은 등수 - 1)
# W < 0 면 팁 X
# 손님의 순서를 적절히 바꿨을 때, 강호가 받을 수 잇는 팁의 최댓값
'''
최대값이 되려면 
가장 첫번째에 큰 값부터 정렬을 해야할듯
'''
import sys

n = int(input())
tipList = [int(sys.stdin.readline().rstrip()) for i in range(n)]
tipList.sort(reverse=True)
result = 0

for i in range(len(tipList)):
    tip = tipList[i] - i
    if tip < 0:
        continue
    result += (tipList[i] - i)

print(result)
