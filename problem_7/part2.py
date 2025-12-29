"""
This function initializes the lasers array with 1 at the starting position and 0 elsewhere.
    Args:
        input: The input string
    Returns:
        A list of lasers, each representing a laser at the starting position
"""
def starting_lasers(input):
    lasers = []
    for idx in range(len(input[0])):
        if input[0][idx] == 'S':
            lasers.append(1)
        else:
            lasers.append(0)
    return lasers

"""
This function updates the lasers array based on the row of the input.
    Args:
        row: The row of the input
        lasers: The list of lasers
    Returns:
        A list of lasers, each representing the timeline count at each index
"""
def update_lasers(row, lasers):
    for idx in range(len(row)):
        if row[idx] == '^' and lasers[idx] > 0:
            lasers[idx - 1] += lasers[idx]
            lasers[idx + 1] += lasers[idx]
            lasers[idx] = 0
    return lasers

def go_to_the_bottom(input, lasers):
    for row in range(1, len(input)):
        new_lasers = update_lasers(input[row], lasers)
        lasers = new_lasers
    return sum(lasers)

input = open('inputs/input.txt', 'r').read()
input = input.split('\n')

lasers = starting_lasers(input)
print(go_to_the_bottom(input, lasers))
