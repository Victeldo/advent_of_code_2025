### We start at 50
### range is 0-99
### Lx moves left by x steps, if spillover, goes to other end and same case for Rx
### need to count how many times we are in position 0
### input is text separateed by newlines, L/R followed by a number


with open('input.txt', 'r') as file:
    input = file.read()

input = input.split('\n')

for line in input:
    if not line.strip():  # Skip empty lines
        continue
    direction = line[0]  # First character is direction (L or R)
    steps = int(line[1:])  # Rest is the number
    print(direction, steps)