flowerbed = [1,0,0,0,1]
'''
[0,1,0,1,0]
'''
n = 1
# 꽃을 심을 수 있는 조건 => i == 0 && planted = False
planted = False # 꽃이 심어져 있는 상태를 나타냄

for i in range(len(flowerbed)):
    if flowerbed[i] == 1:
        if planted: n += 1
        planted = True
    else:
        if not planted and n > 0:
            n -= 1
            planted = True
        else:
            planted = False

if n == 0:
    print(True)
else:
    print(False)

