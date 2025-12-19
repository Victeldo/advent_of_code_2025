with open('input.txt', 'r') as file:
    input = file.read()

input = input.split('\n')


def format_input(input):
    output = []
    for line in input:
        if not line.strip():
            continue
        direction = line[0]
        steps = int(line[1:])
        output.append((direction, steps))
    return output

# print(format_input(input))

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