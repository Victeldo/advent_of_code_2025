
def starting_lasers(input):
    lasers = []
    for idx in range(len(input[0])):
        if input[0][idx] == 'S':
            lasers.append(idx)
    return lasers

def update_lasers(row, lasers, count):
    new_lasers = []
    for idx in range(len(row)):
        if idx in lasers:
            if row[idx] == '^':
                new_lasers.append(idx - 1)
                new_lasers.append(idx + 1)
                count += 1
            else:
                new_lasers.append(idx)
    return new_lasers, count

def go_to_the_bottom(input, lasers):
    count = 0
    for row in range(1, len(input)):
        new_lasers, count = update_lasers(input[row], lasers, count)
        lasers = new_lasers
    return count

input = open('inputs/input.txt', 'r').read()
input = input.split('\n')

lasers = starting_lasers(input)
print(go_to_the_bottom(input, lasers))
