n = int(input())

location = []
xlocation = []

for i in range(n*2):
    if i < n:
        val = list(str(input()))
        location.append(val)
    else:
        val = list(str(input()))
        xlocation.append(val)

resultList = [[0 for i in range(n)] for j in range(n)]


for i in range(n):
    for j in range(n):
        if xlocation[i][j] == 'x':
            resultList[i][j] = 0
        else:
            resultList[i][j] = '.'

for i in range(n):
    for j in range(n):
        if location[i][j] == '*':
            if isinstance(resultList[i][j-1],int):
                try:
                    resultList[i][j-1] += 1
                except IndexError:
                    pass
            elif isinstance(resultList[i][j+1],int):
                try:
                    resultList[i][j+1] += 1
                except IndexError:
                    pass
            elif isinstance(resultList[i-1][j],int):
                try:
                    resultList[i-1][j] += 1
                except IndexError:
                    pass
            elif isinstance(resultList[i-1][j+1],int):
                try:
                    resultList[i-1][j+1] += 1
                except IndexError:
                    pass
            elif isinstance(resultList[i-1][j-1],int):
                try:
                    resultList[i-1][j-1] += 1
                except IndexError:
                    pass
            elif isinstance(resultList[i+1][j],int):
                try:
                    resultList[i+1][j] += 1
                except IndexError:
                    pass
            elif isinstance(resultList[i+1][j-1],int):
                try:
                    resultList[i+1][j-1] += 1
                except IndexError:
                    pass
            elif isinstance(resultList[i+1][j+1],int):
                try:
                    resultList[i+1][j+1] += 1
                except IndexError:
                    pass

print(resultList)




