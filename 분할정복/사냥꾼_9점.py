import sys
input = sys.stdin.readline

m,n,l = map(int,input().split())
target = list(map(int,input().split(sep=' ',maxsplit=m)))
coordinate = []

for i in range(n):
    x,y = map(int,input().split())
    coordinate.append([x,y])

left = 0
right = m
cnt = 0
while left < right:
    check_idx = []
    for i in range(len(coordinate)):
        x = coordinate[i][0]
        y = coordinate[i][1]
        distance_left = abs(target[left]-x) + y
        if distance_left <= l:
            check_idx.append(i)
            cnt += 1
    if len(target) > 1:
        if check_idx:
            for i in check_idx:
                del coordinate[i]


    left += 1

print(cnt)


