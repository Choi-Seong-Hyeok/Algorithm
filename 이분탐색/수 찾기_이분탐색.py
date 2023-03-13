N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))


A.sort()

def binary_search(A,x):
    start = 0
    end = len(A)-1
    while(start <= end):
        m = (start + end)//2
        if(A[m] == x):
            return 1
        elif(A[m]>x):
            end = m -1
        else:
            start = m+1



# B에 대해 이진 검색을 수행합니다.
for i in range(M):
    print(binary_search(A,B[i]))

