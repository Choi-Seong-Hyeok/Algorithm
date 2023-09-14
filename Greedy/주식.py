'''
    1. 하나를 산다 
    2. (개수에 상관없이 최대의 이익이되는대로)판다
    3. 아무것도 안한다.
앞에서부터 주식을 팔되

A. 
맨뒷값이 최대값이라 생각하고 팔다가 
그 값보다 더 큰 값이 나오면 그 값 기준으로 판다.
'''
T = int(input())

for i in range(T):
    dayN = int(input())
    stockList = list(map(int,input().split()))
    maxStock = stockList[-1]
    result = 0
    for i in range(dayN-2,-1,-1):
        if stockList[i] > maxStock:
            maxStock = stockList[i]
        else:
            result += (maxStock - stockList[i])
    print(result)



        
    





