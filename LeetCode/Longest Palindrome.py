class Solution(object):
    def longestPalindrome(self, s):
        S = list(set(s))
        answer = 0
        flag = False
        maxEven = []
        for i in range(len(S)):
            cnt = s.count(S[i])
            if cnt % 2 ==0:
                answer += cnt
            elif cnt % 2 ==1 and cnt > 2:
                maxEven.append(cnt)
            elif cnt == 1:
                flag = True

            if len(maxEven) == 0:
                return answer + flag
            elif len(maxEven) == 1:
                return answer + sum(maxEven)
            else:
                return answer + sum(maxEven) - (len(maxEven)- 1)
            
