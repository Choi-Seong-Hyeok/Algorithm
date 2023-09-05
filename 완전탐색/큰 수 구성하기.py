from itertools import product

'''
    중복을 허용한 모든 수 가운데 N보다 작은 수의 max
    가장 큰 수
'''

N,K_num =map(int,input().split())
K = list(map(str,input().split()))
K = sorted(K)
maxList = []
num = len(str(N))
for i in product(K,repeat=num):
    val = ''.join(i)
    val = int(val)
    if val > N:
        break
    maxList.append(val)
if not maxList:
    for i in product(K,repeat=num-1):
            val = ''.join(i)
            val = int(val)
            maxList.append(val)


print(maxList[-1])

