import sys
input = sys.stdin.readline
'''

D[i] : 마지막으로 뽑은 수가 a[i]일때 가장 긴 부분수열의 길이

지금까지 만들어 놓은 증가수열에 a[i]를 붙일 수 있으려면
    - 만들어 놓은 증가수열이 a[i]보다 앞에 있어야하고 (j < i)
    - 마지막 수가 a[i]보다 작아야 한다.(a[j] < a[i])

    '''
n = int(input())
arr = list(map(int, input().split()))

# dp 테이블 1로 초기화
dp = [1 for _ in range(n)]

for i in range(1,n):
    for j in range(0,i):
        if arr[j] < arr[i]:
            # 더 긴 길이를 찾아가는 과정 (?)
            dp[i] = max(dp[i],dp[j]+1)
result = max(dp)
print(result)


