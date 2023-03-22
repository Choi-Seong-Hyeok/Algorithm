import sys
input = sys.stdin.readline

'''
0부터 배열의 max - 1까지 ! 다시 돌려
'''
def dfs(v):
    pass


n = int(input().rstrip())
rain_list = []
print(rain_list,end='\n')
for _ in range(n):
    arr = list(map(int,input().rstrip().split()))
    rain_list.append(arr)

max_val = max(max(rain_list))
result_list = []

for i in range(max_val):
    dfs(i)

