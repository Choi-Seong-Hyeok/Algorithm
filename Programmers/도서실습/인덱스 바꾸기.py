my_string = "hello"
num1 = 1
num2 = 2

before = my_string[num1]
after = my_string[num2]

answer = list(my_string)
answer[num1] = after
answer[num2] = before

result = ''.join(answer)
print(result)