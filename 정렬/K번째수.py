import sys
input = sys.stdin.readline


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer = []

for i in range(len(commands)):
    cut_i = commands[i][0]
    cut_j = commands[i][1]
    cut_k = commands[i][2]
    cut_arr = array[cut_i - 1:cut_j]
    cut_arr.sort()
    val = cut_arr[cut_k-1]
    answer.append(val)

print(answer)