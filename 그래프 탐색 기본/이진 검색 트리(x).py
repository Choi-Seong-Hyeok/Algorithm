import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

'''

입력받은 전위순회 값들의 리스트에 0번째 값은 root값이다.
root 값보다 큰 값을 pivot 변수에 저장.
이 변수를 기준으로 두 재귀함수를 만들 수 있다.

1. left recursion
2. right recursion
3. print root


'''

def postOrder(start,end):
    if start > end:
        return
    root = preOrder[0]
    pivot = end + 1

    for i in range(start + 1,end + 1):
        if preOrder[i] > root:
            pivot = i
            break
    postOrder(start+1,pivot - 1)
    postOrder(pivot,end)
    print(root)





preOrder = []
while True:
    try:
        val = int(input().rstrip())
        preOrder.append(val)
    except:
        break
if preOrder:
    postOrder(0,len(preOrder)-1)
