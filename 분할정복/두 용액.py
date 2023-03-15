import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
arr.sort()
minValue = sys.maxsize
result = []
left = 0
right = n-1
while left < right:
    total = arr[left] + arr[right]

    if abs(total) < minValue:
        minValue = abs(total)
        result = [arr[left],arr[right]]
    
    if total < 0 :
        left += 1
    else:
        right -= 1


print(result[0],result[1])