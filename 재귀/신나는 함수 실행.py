import sys
input = sys.stdin.readline





while(True):
    a,b,c = map(int,sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break
    def recur(a,b,c):
        if a <= 0 or b <= 0 or c<=0:
            return 1
        if a > 20 or b > 20 or c > 20:
            return recur(20,20,20)
    
        # if a<b and b<c:
        #     return recur(a,b,c-1) + recur(a,b-1,c-1) - recur(a,b-1,c)
        else:
            return recur(a-1,b,c) + recur(a-1,b-1,c) + recur(a-1,b,c-1) - recur(a-1,b-1,c-1)
    
    print('w(',a,',',b,',',c,') = ',recur(a,b,c))
        
    
    



