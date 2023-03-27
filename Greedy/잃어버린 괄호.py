sik_minus = input().split('-') # 55-50+40 => [55, 50+40]
sik_plus = [] #[55, 90]
 
for i in sik_minus: 
    count = 0 
    i = i.split('+') #[55], [50,40]
    for j in i:
        count += int(j) # 1. 55    2. 50+40 
    sik_plus.append(count) 
 
result = sik_plus[0]
for i in range(1, len(sik_plus)):
    result -= sik_plus[i]
 
print(result) # -35