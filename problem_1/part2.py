with open('input.txt', 'r') as file:
    input = file.read()

input = input.split('\n')


"""
This function formats the input into a list of tuples, each containing a direction and a number of steps.
    Args:
        input: The input string
    Returns:
        A list of tuples, each containing a direction and a number of steps
"""
def format_input(input):
    output = []
    for line in input:
        if not line.strip():
            continue
        direction = line[0]
        steps = int(line[1:])
        output.append((direction, steps))
    return output

"""
This function calculates the new position after moving in a given direction for a given number of steps. It also counts how many times the position is 0 while moving.
    Args:
        current_position: The current position on the range 0-99
        direction: The direction to move in, either 'L' or 'R'
        steps: The number of steps to move
    Returns:
        The new position on the range 0-99
        The number of times the position is 0 while moving
"""
def calculate_position(current_position, direction, steps):
    displacement = steps if direction == 'R' else -steps
    final_position = current_position + displacement

    if direction == 'L':
        zero_count = abs((current_position - 1) // 100 - (final_position - 1) // 100)

    elif direction == 'R':
        zero_count = abs((final_position) // 100 - (current_position) // 100)
    
    return final_position % 100, zero_count


"""
This function counts the number of times the position hits 0 after all the moves have been made.
    Args:
        input: The input string
    Returns:
        The number of times the position is 0
"""
def count_zeros(input):
    current_position = 50
    total_zero_count = 0
    moves = format_input(input)
    for direction, steps in moves:
        current_position, zero_count = calculate_position(current_position, direction, steps)
        total_zero_count += zero_count

    return total_zero_count

zero_count = count_zeros(input)
print(zero_count)