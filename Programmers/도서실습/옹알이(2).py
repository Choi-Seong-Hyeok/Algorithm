from itertools import permutations

babbling_list = ["aya", "ye", "woo", "ma"]
babbling = ["ayayeayayeaya"]


answer = 0
for i in range(1,5):
    permuBabbling = list(permutations(babbling_list,i))
    # print(permuBabbling)
    # print(' --- ',i,' 번째 끗 ---')
    #print('길이 : ',len(permuBabbling))
    for j in range(len(permuBabbling)):
        s = ''.join(permuBabbling[j])
        print(s)
        if s in babbling:
            answer += 1
        
    #     for k in str(permuBabbling[j]):
    #         print(k)
print(answer)
            
'''
1. join내장함수 --> tuple 자료형을 str 합치는
2. permutation , combination
'''


# print(total)