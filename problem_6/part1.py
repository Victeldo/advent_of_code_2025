### input is vertically stacked, need to make a grid, i.e. each row is an array (and each vertical column/parallel index is a problem)
### need to add all the vertical problems together to get the total score. Each row is separated by spaces
import math

input = open('inputs/input.txt', 'r').read()

input = input.split('\n')

grid = []

for line in input:
    values = line.split()
    grid.append(values)

operators = grid.pop() ## such that the grid only contains the numbers
### length of grid is the number of args + operator for a problem. length of any row is the number of problems.

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

final_score = 0
for index, operator in enumerate(operators):
    if operator == '+':
        final_score += (add_problems(grid, index))
    elif operator == '*':
        final_score += (multiply_problems(grid, index))

print(final_score)