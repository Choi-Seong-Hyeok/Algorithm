'''

자신의 바로 다음이나 전에 경기하는 팀에게만 카약을 빌려줌
--> 팀 4는 여분의 카약을 3이나 5에게만 빌려줌 
--> 다른 팀에게서 받은 카약은 다른 이에게 빌려줄수없음
--> 여분의 카약을 가져온 팀의 카약이 손상되었을때 빌려줄수없음

출력은 len(hurtTeam)?

    반례 

    5 2 2
    2 4     
    2 4
카약을 하나 더 가져온 팀이 손상되었을경우

# 1

10 1 1

1 3

정답: 1
고칠 배가 처음부터 없는 경우 
'''

# 팀의 수 N, 카약이 손상된 팀의 수 S, 카약을 하나 더 가져온 팀의 수 R
n, s, r = map(int, input().split())

demaged = list(map(int,input().split()))
extra = list(map(int,input().split()))

# 카약 정보를 가지는 리스트 생성 후 1으로 초기화
list1 = [1] * n

# 손상된 카약을 가진 팀 = 0 
for i in demaged:
    list1[i-1] -= 1

# 여분의 카약을 가진 팀 = 2
for j in extra:
    list1[j-1] += 1

for k in range(len(list1)):
    # 손상된 카약을 가진 팀이라면
    if list1[k] == 0:
        # 첫번째 원소일때
        if k == 0:
            if list1[k+1] == 2:
                list1[k+1] = 1
                list1[k] = 1
        # 마지막 원소일때
        elif k == len(list1)-1:
            if list1[k-1] == 2:
                list1[k-1] = 1
                list1[k] = 1
        # 중간 원소일때
        else:
            if list1[k-1] == 2:
                list1[k-1] = 1
                list1[k] = 1
                continue              
            if list1[k+1] == 2:
                list1[k+1] = 1
                list1[k] = 1
                continue
    else:
        continue
print(list1.count(0))



