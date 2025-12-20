

input = open('inputs/input.txt', 'r').read()

input = input.split(',')

total_sum = 0
pairs = []

for line in input:
    pair = line.split('-')
    pairs.append((int(pair[0]), int(pair[1])))

def count_invalid(start, end):
    invalid_sum = 0

    for i in range(start, end + 1):
        string_i = str(i)
        if len(string_i) % 2 == 0:
            if string_i[len(string_i)//2:] == string_i[:len(string_i)//2]:
                invalid_sum += i
    return invalid_sum


for pair in pairs:
    total_sum += count_invalid(pair[0], pair[1])
print(total_sum)
