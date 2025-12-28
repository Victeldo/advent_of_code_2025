def add_problems(numbers):
    total_score = 0
    for number in numbers:
        total_score += number
    
    return total_score

def multiply_problems(numbers):
    total_score = 1
    for number in numbers:
        total_score *= number
    
    return total_score

def find_whitespace_columns(input):
    whitespace_columns = []
    for i in range(len(input[0])):
        if all(input[j][i] == ' ' for j in range(len(input))):
            whitespace_columns.append(i)
    return whitespace_columns

"""
This function formats the input into a grid of numbers and operators.
    Args:
        input: The input string
        whitespace_columns: The columns that are whitespace
    Returns:
        A grid of numbers and operators
    Note: The whitespace_columns are used to split the numbers into separate "raw" numbers.
    We maintain the whitespace columns so that we can correctly format the numbers from
    horizontal to vertical representation.
"""
def format_grid(input):
    whitespace_columns = find_whitespace_columns(input)
    grid = []
    for line in input:
        values = []
        current_value = ''
        for i in range(len(line)):
            if i in whitespace_columns:
                values.append(current_value)
                current_value = ''
            else:
                current_value += line[i]
        values.append(current_value)
        grid.append(values)
    operators = grid.pop()
    operators = [operators.strip() for operators in operators]
    return grid, operators

"""
This function formats the numbers into a list of numbers.
    Args:
        grid: The grid of numbers and operators
        index: The index of the column to format
    Returns:
        A list of numbers
    Note: The index is the column index of the numbers to format. It takes the raw numbers
    and concatenates the digits top to bottom (and strips the whitespace).
"""
def format_numbers(grid, index):
    numbers = []

    for row in grid:
        numbers.append(row[index])

    formatted_numbers = []
    for digit in range(len(numbers[0])):
        concatenated = ''
        for number in numbers:
            concatenated += number[digit]
        formatted_numbers.append(int(concatenated.strip()))
    return(formatted_numbers)

def cephalopod_math(grid, operators):
    total = 0
    for index, operator in enumerate(operators):
        numbers = format_numbers(grid, index)
        if operator == '+':
            total += add_problems(numbers)
        elif operator == '*':
            total += multiply_problems(numbers)
    return total

input = open('inputs/input.txt', 'r').read()
input = input.split('\n')

grid, operators = format_grid(input)

print(cephalopod_math(grid, operators))
