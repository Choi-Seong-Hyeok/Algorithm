
x = input()
a = 'AAAA'
b = 'BB'
ab = 'AAAABB'
result = ''

cnt = 0
for i in x:
    if i == 'X':
        cnt += 1
    elif i == '.':
        if cnt == 6:
            result += ab + '.'
        elif cnt == 4:
            result += a + '.'
        elif cnt == 2:
            result += b + '.'
        cnt = 0
        result += '.'
print('result : ',result)
# cntString = x.count('X')
# if result == "" :
#     if cntString == 6:
#         print(ab)
#     if cntString == 4:
#         print(a)
#     if cntString == 2:
#         print(b)
# else:
#     print(result)

