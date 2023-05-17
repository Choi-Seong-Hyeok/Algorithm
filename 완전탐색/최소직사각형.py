import sys
input = sys.stdin.readline

n,m = map(int,input().split())

my_list = []
big = []
small = []

for i in range(n):
    my_list.append(list(map(int, input().split())))

for i in range(n):
    if my_list[i][0] > my_list[i][1]:
        big.append(my_list[i][0])
        small.append(my_list[i][1])
    else:
        big.append(my_list[i][1])
        small.append(my_list[i][0])

print(big)
print(small)

print(max(big) * max(small))