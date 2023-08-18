'''
C = id , age , room , dep.
즉 정수만 있는 열의 이름을 나타냄
C가 주어지면 그 열에 있는 최대값을 반환

1. C의 인덱스를 찾고
2. 그 인덱스를 가지고 잘라낸 각 리스트의 인덱스를 추출하여 특정 배열에 추가
3. 그 배열의 맥스 값이 답

'''
S = "city,temp2,temp\nParis,7,-3,\nDubai,4,-4\nPorto,-1,-2"
C = "temp"
findMaxList = []
totalList= S.split("\n")
print('totalList : ',totalList)
nameList = list(totalList[0].split(','))
print('nameList : ',nameList)
#findIndex = [i for i in range(len(nameList)) if C in nameList[i]]
for i in range(len(nameList)):
    if nameList[i] == C:
        findIndex = i
# --- 
# findIndex = findIndex[0]
print('findIndex : ',findIndex)
for i in range(1,len(totalList)):
    findArray = list(totalList[i].split(','))
    print('findArray : ',findArray)
    findMaxList.append(int(findArray[findIndex]))

print('findMaxList : ',max(findMaxList))

print(max(findMaxList))

#print(int(max(findMaxList)))

# print('A의 NUM : ',len(A))
# listA = A[0]
# findIndex = listA.index(C)
# print(findIndex)
# splitListA = listA.split(',')
# num = len(splitListA)
# print(num)


def solution(S, C):
    # Implement your solution here
    findMaxList = []
    totalList= S.split("\n")
    nameList = list(totalList[0].split(','))
    findIndex = [i for i in range(len(nameList)) if C in nameList[i]]
    findIndex = findIndex[0]

    for i in range(1,len(totalList)):
        findArray = list(totalList[i].split(','))
        findMaxList.append(findArray[findIndex])

    return int(max(findMaxList))