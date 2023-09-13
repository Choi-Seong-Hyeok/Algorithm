'''
준현 - 살수있는 최대 만큼 사고 존버
성민 - 내가 가지고 있는 주식이 3일 연속 상승시 다음날 매도
    - 3일 연속 하락하는 주식은 다음날 무조건 가격 상승 So 주식 전량 매수
1월 14일의 자산은 (현금 + 1월 14일의 주가 × 주식 수)
stockCnt * i
'''
Money = int(input())
MachineDuck = list(map(int,input().split()))
JMoney = Money # 준현이의 돈
SMoney = Money # 성민이의 돈
resultStock = 0
Jasset = 0 # 준현이의 자산
Sasset = 0 # 성민이의 자산

for i in MachineDuck:
    stockCnt = JMoney // i
    if stockCnt:
        JMoney -= (i * stockCnt)
        resultStock += stockCnt
    if JMoney <= 0:
        break

Jasset = (JMoney + (MachineDuck[-1]*resultStock)) # 준현이의 최종 자산
resultStock = 0 # 초기화
stockCnt = 0 # 초기화
currentStock = 0 # 비교 주식
currentAsset = 0 

for i in range(len(MachineDuck)):
    if i == 10:
        break
    # 3일 연속 하락하는 주식
    if MachineDuck[i] > MachineDuck[i+1] and MachineDuck[i+1] > MachineDuck[i+2]:
        stockCnt = SMoney // MachineDuck[i+3]
        if stockCnt:
            SMoney -= (MachineDuck[i+3] * stockCnt)
            resultStock += stockCnt
    if resultStock and MachineDuck[i+1] > MachineDuck[i] and MachineDuck[i+2] > MachineDuck[i+1]:
        currentAsset = (SMoney + (MachineDuck[i+3]*resultStock))

currentAsset += SMoney
Sasset = currentAsset

if Jasset > Sasset:
    print("BNP")
elif Jasset == Sasset:
    print("SAMESAME")
else:
    print("TIMING")






