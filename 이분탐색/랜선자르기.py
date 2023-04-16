import sys
input = sys.stdin.readline

k,n = map(int,input().rstrip().split())
LAN = []
# 랜선의 길이
for _ in range(k):
    LAN.append(int(input()))
# 오름차순 정렬
LAN.sort()
# start 값은 0이될수없다
left = 1
# end 값은 max(LAN)
right = LAN[k-1]

while left <= right:
    # target value
    mid = (left + right) // 2
    cnt = 0
    # 랜선의 길이를 mid로 잘랐을때 길이 구하기
    for i in LAN:
        if i >= mid:
            cnt += (i // mid)
    # 생각보다 덜 잘렸으면 right를 앞으로 땡겨
    if cnt < n:
        right = mid - 1
    # 생각보다 더 잘렸으면 left를 뒤로 땡겨
    else:
        left = mid + 1


print(right)

