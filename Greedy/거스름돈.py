# 나머지 = n - (5 * 몫) 

n = int(input())

cnt = 0
val = n // 5
remainder = 0
while 1:
    if n == 1 or n == 3: # n이 1 or 3이면 pass
        cnt = -1
        break
    remainder = n - (5 * val)
    cnt = val
    if remainder == 0: # 나머지가 0
        break
    if remainder % 2 == 0: # 나머지가 2의 배수로 떨어지는경우 경우
        cnt += (remainder // 2)
        break
    else:
        val -= 1 # 몫을 1 줄임
        cnt = 0 # cnt 값은 초기화


print(cnt)