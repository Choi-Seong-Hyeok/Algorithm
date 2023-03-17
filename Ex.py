
answer = 1
target = 0
zero = 0
def solution(n):
    global zero
    global target
    global answer

    if n == 0:
        return 0
    else:
        x = n + solution(n+1)
        if x == target:
            answer += 1
        return
        
            

print('답은요 : ',solution(15))