def solution(my_string):
    my_string = my_string.split()
    answer = int(my_string[0])
    
    for i in range(len(my_string)):  
        if my_string[i] == '+':
            answer = answer + int(my_string[i+1])
        if my_string[i] == '-':
            answer = answer - int(my_string[i+1])
    return answer