
a,b = map(int,input().rstrip().split())

max = 0
min = 0
a = str(a)
b = str(b)
a_min , a_max ,b_min , b_max = "","","",""

a_min = a.replace('6','5')
a_max = a.replace('5','6')

b_min = b.replace('6','5')
b_max = b.replace('5','6')

max = int(a_max) + int(b_max)
min = int(a_min) + int(b_min)

print(min , max)