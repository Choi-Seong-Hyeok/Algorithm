x = input()


result = x.replace('XXXX','AAAA')
result = result.replace('XX','BB')

if 'X' in result:
    print(-1)
else:
    print(result)