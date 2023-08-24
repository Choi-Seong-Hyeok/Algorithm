def solution(A, B):
    cnt = 0
    answer = 0
    target = False
    for i in range(len(A)):
        if A == B:
            target = True
            break
        A = A[-1] + A[:len(A)-1]
        cnt += 1

    if target == True:
        answer = cnt
    else:
        answer = -1
    return answer