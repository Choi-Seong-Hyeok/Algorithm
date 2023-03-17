

def expression(n,i,result):
    if n > result:
        return False
    if result == n:
        return True
    n += i
    return expression(n,i+1,result)




def solution(n):
    answer = 0
    for i in range(n):
        if expression(0,i+1,n):
            answer += 1
    return answer

print(solution(15))