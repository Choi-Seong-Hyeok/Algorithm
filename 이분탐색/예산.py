import sys
input = sys.stdin.readline

n = int(input())

budget_list = list(map(int,input().rstrip().split()))
budget_list.sort()
max_budget = int(input())
right = budget_list[n-1]
left = 0

# 모든 예산을 배정해도 부족함이 없을 경우
if sum(budget_list) <= max_budget:
    print(right)
# 아닌 경우
else:
    while left <= right:
        # target 설정 mid
        mid = (left+right)//2
        # 총 예산 
        total_budget = 0
        # mid 값과 비교하여 최소값을 더함
        for i in budget_list:
            total_budget += min(i,mid)
        # 이분탐색 과정
        if total_budget > mid:
            right = mid - 1
        else:
            left = mid + 1
        
print(mid)


