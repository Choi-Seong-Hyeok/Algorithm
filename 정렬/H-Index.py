def solution(citations):
    more = 0
    less = 0
    val = []
    for i in range(len(citations)):
        target = i
        for j in range(len(citations)):
            if citations[j] >= target:
                     more += 1
            elif citations[j] <= target:
                      less += 1
        if less <= target and more >= target:
            val.append(target)
        more = 0
        less = 0

    
    answer = max(val)
    
    return answer