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
This function calculates the new position after moving in a given direction for a given number of steps. It also handles the spillover case where the position is less than 0 or greater than 99.
    Args:
        current_position: The current position on the range 0-99
        direction: The direction to move in, either 'L' or 'R'
        steps: The number of steps to move
    Returns:
        The new position on the range 0-99
"""
def calculate_position(current_position, direction, steps):
    if direction == 'L':
        current_position -= steps
    elif direction == 'R':
        current_position += steps
    
    if current_position < 0:
        while current_position < 0:
            current_position += 100
    elif current_position > 99:
        while current_position > 99:
            current_position -= 100
    return current_position

"""
This function counts the number of times the position is 0 after all the moves have been made.
    Args:
        input: The input string
    Returns:
        The number of times the position is 0
"""
def count_zeros(input):
    current_position = 50
    zero_count = 0
    moves = format_input(input)
    for direction, steps in moves:
        current_position = calculate_position(current_position, direction, steps)
        if current_position == 0:
            zero_count += 1
    return zero_count

zero_count = count_zeros(input)
print(zero_count)

### thinking out loud. if we were to manually bruteforce it, lest think about solving going left and right respectively.
### going right is the simple case. if we are at a nonzero number and we wrap around, we just add the number of wraps (even if we land on 0)
### going left is the tricky case. if we go left from a nonzero number, its simple, just wrap around and add the number of wraps (even if we land on 0)
### if start at p, and move right, k times, we can calculate landing on zero as (p + k) % 100 == 0. i.e. k = (100 - p) % 100
### if p = 0, 

### if start at p, and move left, k times, we can calculate landing on zero as (p - k) % 100 == 0. i.e. k = p % 100
