import sys

input = sys.stdin.readline

def mergeLR(x,y):
    result = []
    i, j = 0,0

    while i < len(x) and j < len(y):
        if x[i] < y[j]:
            result.append(x[i])
            i += 1
        else:
            result.append(y[j])
            j += 1
            
    if i == len(x):
        while j < len(y):
            result.append(y[j])
            j += 1
    elif j == len(y):
        while i < len(x):
            result.append(x[i])
            i += 1
    return result

def mergeSort(x):
    if len(x) <= 1:
        return x
    else:
        # 나누기 
        div = len(x) // 2
        left = mergeSort(x[:div])
        right = mergeSort(x[div:])
        # 합치기
        return mergeLR(left,right)
        


n = int(input().rstrip())
l = []
for i in range(n):
    val  = int(input())
    l.append(val)

print('정렬 전 : ',l)
print('정렬 후 : ',mergeSort(l))

