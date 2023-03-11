import sys
# 채점하면 틀리긴함
n, c = map(int, sys.stdin.readline().split())
houses = []
for _ in range(n):
    houses.append(int(sys.stdin.readline()))


houses.sort()

start = houses[0]
end = houses[-1] - houses[0]
result = 0

while start <= end:
    mid = (start+end)//2

    cnt = 1
    currentHouse = houses[0]
    for house in houses:
        if house >= currentHouse + mid:
            cnt += 1
            currentHouse = house

    if cnt >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
