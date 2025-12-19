### We start at 50
### range is 0-99
### Lx moves left by x steps, if spillover, goes to other end and same case for Rx
### need to count how many times we are in position 0
### input is text separateed by newlines, L/R followed by a number


current_position = 50
zero_count = 0

def calculate_position(current_position):
    if current_position in range(0, 100):
        return current_position
    elif current_position > 99:
        ### need to keep subtracting 100 until we are in range 0-99
        while current_position > 99:
            current_position -= 100
        return current_position
    elif current_position < 0:  
        ### need to keep adding 100 until we are in range 0-99
        while current_position < 0:
            current_position += 100
        return current_position

with open('input.txt', 'r') as file:
    input = file.read()

input = input.split('\n')

for line in input:
    if not line.strip():  # Skip empty lines
        continue
    direction = line[0]  # First character is direction (L or R)
    steps = int(line[1:])  # Rest is the number
    if direction == 'L':
        current_position -= steps
    elif direction == 'R':
        current_position += steps
    
    ### need to make sure it spillsover and calculates the current position correctly e.g. if we are at 5 and move left by 100, then we should be at (5-100 = 95 = 4) but if we are at 95 and move left by 100, then we should be at (95-100 = 94 = 4)
    current_position = calculate_position(current_position)
    if current_position == 0:
        zero_count += 1

print(zero_count)