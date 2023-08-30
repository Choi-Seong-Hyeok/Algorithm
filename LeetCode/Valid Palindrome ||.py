'''
    1. 반복문 안에서 해당 단어가 홀수 개수 or 짝수 개수인지 체크
    2. 짝수면 패스 
    2-1. 홀수면 해당 단어를 지우고 Palindrome인지 Check(함수)
    abca
    1) aabc
    2) caab
    3) bcaa
    4) abca (X)

    "aca"
    1)aac
    2)caa
    3)aca
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i <= j:
            if s[i] != s[j]:
                break
            i += 1
            j -= 1
        if i > j: 
            return True

        # 오른쪽에 1개 지우기
        i = 0
        j = len(s)-1
        once = False
        while i <= j:
            if s[i] != s[j] and not once:
                j -= 1
                once = True
                continue
            elif s[i] != s[j]:
                break
            i += 1
            j -= 1
        if i > j: 
            return True

        # 왼쪽에 1개 지우기
        i = 0
        j = len(s)-1
        once = False
        while i <= j:
            if s[i] != s[j] and not once:
                i += 1
                once = True
                continue
            elif s[i] != s[j]:
                break
            i += 1
            j -= 1
        if i > j: 
            return True




