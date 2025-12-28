## downward count the indices we have beams.
## we need to count how many times a split is rendered, so basically when we update the downward beam count, we also update a counter for the split.

"""
pseudocode:
lasers = [] ## start with index of S
go down a row, if row[x] == lasers[x] update new list to have left and right indices, and not original and add to the split count.
if no split, just retain the original index.
"""

input = open('inputs/input.txt', 'r').read()
input = input.split('\n')

lasers = []
for idx in range(len(input[0])):
    if input[0][idx] == 'S':
        lasers.append(idx)


count = 0
for round in range(1, len(input)):
    new_lasers = []
    for idx in range(len(input[round])):
        if idx in lasers:
            if input[round][idx] == '^':
                new_lasers.append(idx - 1)
                new_lasers.append(idx + 1)
                count += 1
            else:
                new_lasers.append(idx)
    lasers = new_lasers

print(count)
