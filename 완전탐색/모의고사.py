def solution(answers):
    answer = []
    cnt = [0,0,0]
    mathGiveup1 = [1,2,3,4,5]
    mathGiveup2 = [2,1,2,3,2,4,2,5]
    mathGiveup3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        if answers[i] == mathGiveup1[(i%5)]:
            cnt[0] += 1
        if answers[i] == mathGiveup2[(i%8)]:
            cnt[1] += 1
        if answers[i] == mathGiveup3[(i%10)]:
            cnt[2] += 1
    
    for i in range(3):
        if cnt[i] == max(cnt):
            answer.append(i+1)
    
    
    return answer