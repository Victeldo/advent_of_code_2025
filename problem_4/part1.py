### input is 2x2 matrix of . or @, gotta make a grid, from lines of input into 2d array. then need to find number of @ surrounded by less than 4 @.

input = open('inputs/input.txt', 'r').read()
grid = []
for line in input.split('\n'):
    grid.append(list(line))

safe_count = 0
# i is row, j is column
for i in range(len(grid)):
    for j in range(len(grid[0])):
        surrounding_count = 0
        if grid[i][j] == '@':
            ## need to check up, down, left, right, and diagonals -- and also if out of bounds, skip

            ## check up (skip if i is 0) and then top left and top right
            if i > 0:
                if grid[i-1][j] == '@':
                    surrounding_count += 1
                if j > 0:
                    if grid[i-1][j-1] == '@':
                        surrounding_count += 1
                if j < len(grid[0]) - 1:
                    if grid[i-1][j+1] == '@':
                        surrounding_count += 1
            ## check down (skip if i is len(grid) - 1) and then bottom left and bottom right
            if i < len(grid) - 1:
                if grid[i+1][j] == '@':
                    surrounding_count += 1
                if j > 0:
                    if grid[i+1][j-1] == '@':
                        surrounding_count += 1
                if j < len(grid[0]) - 1:
                    if grid[i+1][j+1] == '@':
                        surrounding_count += 1
            ## check left (skip if j is 0)
            if j > 0:
                if grid[i][j-1] == '@':
                    surrounding_count += 1
            ## check right (skip if j is len(grid[0]) - 1)
            if j < len(grid[0]) - 1:
                if grid[i][j+1] == '@':
                    surrounding_count += 1
            
            if surrounding_count < 4:
                safe_count += 1

print(safe_count)
