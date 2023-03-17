import sys
input = sys.stdin.readline

'''
필요한 변수 및 리스트들
1. n개의 체크 리스트
2. 합치기 전 현재 리스트
3. 최종적인 중복이 없는 set 자료
4. 입력받은 전체 리스트
'''

n = int(input())
k = int(input())

card = [int(input()) for _ in range(n)]
check = [False for _ in range(n)]
current_list = []
result = set()

def recur(k):
    # 바닥 조건
    if k == 0:
        a = ""
        for i in current_list:
            a += str(i)
        result.add(a)
    else:
        for i in range(n):
            if check[i] : continue
            check[i] = True
            current_list.append(card[i])
            recur(k-1)
            current_list.pop()
            check[i] = False

recur(k)
print(len(result))

