my_string = "o11111o1111o"
my_string = list(my_string)

result = []
val = ""
target = True
for str in my_string :
    asciiNumber = ord(str)
    if asciiNumber >= 65 :
        result.append(val)
        val = ""
        pass
    elif asciiNumber >= 48 and asciiNumber <= 57:
        val += str
    else:
        pass
realList = []
result.append(val)
for i in result:
    if i == '':
        pass
    else:
        realList.append(int(i))
print(sum(realList))
