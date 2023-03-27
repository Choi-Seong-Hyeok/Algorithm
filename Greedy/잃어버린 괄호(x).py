import sys
input = sys.stdin.readline

bracket = list(map(str,input().rstrip()))

# 음수 전에 괄호 넣기
check = True

for i in range(len(bracket)):
    # - 나오면 앞에 괄호 '(' 열어주기 
    # cnt 변수로 체크 ? 또는 bool ? 

    if bracket[i] == '-' and check == True:
        bracket.insert(i+1,'(')
        check = False
        continue

    if bracket[i] == '-' and check == False:
        bracket.insert(i-1,')')
        check = True

if check == False and bracket[-1] != ')':
    bracket.append(')')

result = eval(''.join(bracket))
print(result)

    
    