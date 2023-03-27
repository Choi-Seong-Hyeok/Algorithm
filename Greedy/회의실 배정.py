import sys
input = sys.stdin.readline

n = int(input())
time = []


for i in range(n):
    start, end = map(int,input().split())
    time.append([start,end])



# start 기준으로 오름차순 정렬
time = sorted(time, key = lambda a : a[0])
# end 기준으로 오름차순 정렬
time = sorted(time, key = lambda a : a[1])

cnt = 0
last_end = 0

for start,end in time:
    if start >= last_end:
        cnt += 1
        last_end = end
print(cnt)





