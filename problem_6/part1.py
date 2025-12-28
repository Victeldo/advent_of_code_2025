def format_grid(input):
    grid = []
    for line in input:
        values = line.split()
        grid.append(values)
    operators = grid.pop()
    return grid, operators

def add_problems(grid, index):
    total_score = 0
    for row in grid:
        total_score += int(row[index])
    
    return total_score

def multiply_problems(grid, index):
    total_score = 1
    for row in grid:
        total_score *= int(row[index])
    
    return total_score

def cephalopod_total(grid, operators):
    final_score = 0
    for index, operator in enumerate(operators):
        if operator == '+':
            final_score += (add_problems(grid, index))
        elif operator == '*':
            final_score += (multiply_problems(grid, index))
    return final_score

input = open('inputs/input.txt', 'r').read()
input = input.split('\n')
grid, operators = format_grid(input)

print(cephalopod_total(grid, operators))