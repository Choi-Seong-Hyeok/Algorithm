import sys
input = sys.stdin.readline

n = int(input().rstrip())

def star(l):
    if l == 3:
        return ['***','* *','***']

    arr = star(l//3)
    print('이것이 arr 이다 : ',arr)
    stars = []

    for i in arr:
        stars.append(i*3)

    for i in arr:
        stars.append(i+' '*(l//3)+i)

    for i in arr:
        stars.append(i*3)

    return stars

print('\n'.join(star(n)))