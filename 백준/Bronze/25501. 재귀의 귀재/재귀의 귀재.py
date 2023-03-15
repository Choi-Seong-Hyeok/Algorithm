import sys
input = sys.stdin.readline


def recursion(s, l, r,cnt):
    if l >= r: return 1,cnt
    elif s[l] != s[r]: return 0,cnt
    else: 
        cnt += 1
        return recursion(s, l+1, r-1,cnt)

def isPalindrome(s,cnt):
    return recursion(s, 0, len(s)-1,cnt)





t = int(input())
for i in range(t):
    palindrome = str(input().rstrip())
    counter = 1
    result = list(isPalindrome(palindrome,counter))
    for i in result:
        print(i,end=' ')
    print()
    



