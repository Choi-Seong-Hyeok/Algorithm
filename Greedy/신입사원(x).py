'''
서류 기준으로 먼저 오름차순 정렬 후 생각.
'''

import sys 
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    a,b = map(int,input().rstrip().split())
    arr.append([a,b])

arr.sort()
temp = arr[0][1]
cnt = 1 
print(arr)
for i in range(n):
    if temp > arr[i][1]:
        temp = arr[i][1]
        cnt += 1
print(cnt)
