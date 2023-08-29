array = [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]

count = 0
counts_of_zeros = []

for num in array:
    if num == 0:
        count += 1
    else:
        if count > 0:
            counts_of_zeros.append(count)
            count = 0

if count > 0:
    counts_of_zeros.append(count)

print(counts_of_zeros)
