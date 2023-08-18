def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    for i in range(len(citations)):
        if i+1 >= citations[i] and (i+1) <= citations[i]:
            answer = i+1
            return answer
    return answer


citations = [3, 0, 6, 1, 5]
print(solution(citations))