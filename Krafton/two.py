S = "AABBBB"
# A의 마지막 위치 앞의 B들을 cnt -> result 

x = S.rindex("A")
cnt = 0
for i in range(x):
    if S[i] == "B":
        cnt += 1
print(cnt)
