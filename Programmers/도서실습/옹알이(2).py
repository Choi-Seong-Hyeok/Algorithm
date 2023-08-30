babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
babbling_list = ["aya", "ye", "woo", "ma"]

answer = 0
for bb in babbling:
    for ba in babbling:
        bb = bb.replace(ba,' ')
    bb=bb.replace(' ','')
    if len(bb) == 0:
        answer += 1
print(answer)