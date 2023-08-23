def solution(quiz):
    answerList = []

    for q in quiz:
        q = q.split()
        answer = int(q[0])
        result = int(q[-1])

        for j in range(len(q)):
            if q[j] == '+':
                answer += int(q[j+1])
            if q[j] == '-':
                answer -= int(q[j+1])

        if result == answer:
            answerList.append("O")
        else:
            answerList.append("X")

    return answerList