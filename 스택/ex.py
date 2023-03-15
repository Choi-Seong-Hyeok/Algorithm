'''
병합정렬을 구현하기 위해 해야하는 것.
    1. 리스트를 1/2로 쪼갠다.(재귀 사용)
    2. 쪼갠 리스트를 다시 병합(merge)한다.
'''
import sys
def mergeList(l,r):
    # 왼쪽과 오른쪽의 인덱스 값
    i,j = 0, 0
    # 최종 정렬된 리스트
    result = []

    # 두 리스트 값 비교 and 리스트에 작은 값대로 넣기
    while i < len(l) and j < len(r):
        # 막힌 부분: 첫번째 값 어케함  
        # 인덱스끼리 비교 하는게 아닌듯.
        if l[i] < r[j]:
            result.append(l[i])
            i+=1
        else:
            result.append(r[j])
            j += 1
    
    # 나머지 값 몰빵
    if j == len(r):
        while i < len(l):
            result.append(l[i])
            i += 1
    elif i == len(l):
        while j < len(r):
            result.append(r[j])
            j += 1
    return result

def divideList(x):
    if len(x) == 1:
        return x
    else:
        left = []
        right = []
        m = len(x) //2 
        # 막힌 부분 ==> m값 설정 해결.
        
        # 나눈다.
        left = divideList(x[:m])
        right = divideList(x[m:])

        return mergeList(left,right)



    








l = [5,2,4,6,8,3,12,6,2,1]
print('정렬 되기 전 : ',l)
print('정렬 된 후 : ',divideList(l))