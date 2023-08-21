
def solution(my_string):
    
    answer = int(my_string[0])
    
    for i in range(len(my_string)):
        if my_string[i-1] == '+':
            answer = answer + int(my_string[i])
        if my_string[i-1] == '-':
            answer = answer - int(my_string[i])
    return answer

my_string = "3+4"

print(solution(my_string))