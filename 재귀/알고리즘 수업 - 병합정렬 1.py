import sys
input = sys.stdin.readline

def mergeSort(x):
    if len(x) == 1:
        return x
    else:    # 중간 값
        middle = len(x) // 2
        # middle 기준으로 나눠주기
        left = mergeSort(x[:middle])
        right = mergeSort(x[middle:])
        
        return merge(left,right)

def merge(l,r):
    # 각 리스트들의 첫번째 인덱스 값.
    i,j = 0,0
    # 결과 값을 넣을 리스트
    result = []

    # 두 리스트의 작은 인덱스부터 비교하여 작은 값을 result index에 넣기
    while i < len(l) and j < len(r):
        if l[i] > r[j]:
            result.append(r[j])
            ans.append(r[j])
            j += 1
        elif r[j] > l[i]:
            result.append(l[i])
            ans.append(l[i])
            i += 1

    if i == len(l):
        while j < len(r):
            result.append(r[j])
            ans.append(r[j])
            j += 1
    else:
        while i < len(l):
            result.append(l[i])
            ans.append(l[i])
            i += 1
    
    return result







n,k=map(int,input().split())
A = list(map(int,input().split()))
ans = []
mergeSort(A)
if len(ans) >= k:
    print(ans[k-1])
else:
    print(-1)















