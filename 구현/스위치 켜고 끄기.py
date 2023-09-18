'''
    1~N의 랜덤 자연수 하나씩 제공
    1. 남 -> 스위치 번호가 자기가 받은 수의 배수이면 그 스위치 상태를 바꿈
    1-1. 1이면 -> 0 , 0이면 -> 1
    2. 여 -> 그 번호를 중심으로 대칭성 확인 후 
    2-1. 대칭이면 모두 바꾸고 아니면 Pass
'''

N = int(input())
switch = list(map(int,input().split()))
student = int(input())


def isSymmetry(num1,num2):
    if num1 == num2:
        return True
    else:
        return False

for i in range(student):
    gender,number = map(int,input().split())
    if gender == 1:
        # 배수의 스위치 반전 가능한 자연수
        val = N // number
        for i in range(1,val+1):
            if switch[(number*i)-1] == 0:
                switch[(number*i)-1] = 1
            elif switch[(number*i)-1] == 1:
                switch[(number*i)-1] = 0
    else:
        # 대칭의 시작과 끝
        firstIndex = 0
        lastIndex = 0 
        # 번호가 첫번째 또는 맨 끝일 경우
        if number == 1 or number == student:
            pass
        for i in range(1,((number+1)//2)+1):
            if (number-i)-1 < 0 or (number+i)-1 > (N-1):
                break
            if isSymmetry(switch[(number-i)-1],switch[(number+i)-1]):
                firstIndex = (number-i)-1
                lastIndex = (number+i)-1
            else:
                firstIndex = number-1
                lastIndex = number-1
                break
        for i in range(firstIndex,lastIndex+1):
            if switch[i] == 0:
                switch[i] = 1
            else:
                switch[i] = 0

cnt = 0
for i in range(N):
    print(switch[i],end=' ')
    cnt += 1
    if cnt % 20 == 0:
        print()

