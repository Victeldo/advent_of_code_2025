def format_grid(input):
    grid = []
    for line in input:
        values = line.split()
        grid.append(values)
    operators = grid.pop()
    return grid, operators

def add_problems(numbers, index):
    total_score = 0
    for number in numbers:
        total_score += number[index]
    
    return total_score

def multiply_problems(numbers, index):
    total_score = 1
    for number in numbers:
        total_score *= number[index]
    
    return total_score

def cephalopod_total(grid, operators):
    final_score = 0
    for index, operator in enumerate(operators):
        if operator == '+':
            final_score += (add_problems(grid, index))
        elif operator == '*':
            final_score += (multiply_problems(grid, index))
    return final_score

# print(cephalopod_total(grid, operators))


### it is now much trickier. given the columns, we now compose numbers by columns.
"""
64 -> 6 4 0
23 -> 2 3 0
314 -> 3 1 4

top to bottom, we compose numbers by column. adding trailing 0s helps a lot.
so we get 4, 431, 623

so given some column of numbers in strings, we must do the following:
1. find out the longest number in the column, and add trailing #s to make shorter numbers equivalent in length.
1.5 trailing #s is insufficient, we need to make sure to add to correct side, not just blindly to the end
2. string concatenate numbers top to bottom by index. row_0 + row_1 + row_2 + ...
3. convert the concatenated string into an integer and add to a list.
4. repeat this for all columns to get all the numbers.
5. perform the operations in the order of the operators.
"""

def format_numbers(grid, index):
    numbers = []

    ### raw numbers
    for row in grid:
        numbers.append(row[index])
    
    # find longest and add trailing #s
    longest = max(numbers, key=len)
    for idx, number in enumerate(numbers):
        if len(number) < len(longest):
            numbers[idx] += '#' * (len(longest) - len(number))
    
    ## string concatenate each number top to bottom by string index, skipping the #s

    cleaned_numbers = []

    for i in range(len(numbers[0])):
        concatenated = ''
        for idx, number in enumerate(numbers):
            if number[i] != '#':
                concatenated += numbers[idx][i]
        cleaned_numbers.append(int(concatenated))
    
    print(cleaned_numbers)

    # ## string concatenate each number top to bottom by string index (now that all of equal length). row_0 + row_1 + row_2 + ...
    # for i in range(len(numbers[0])):
    #     concatenated = ''
    #     for number in numbers:
    #         concatenated += number[i]
    #     numbers.append(concatenated)
    
    # return numbers


input = open('inputs/input1.txt', 'r').read()
input = input.split('\n')
grid, operators = format_grid(input)
print(format_numbers(grid, 0))
