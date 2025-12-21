def build_grid(input):
    grid = []
    for line in input.split('\n'):
        grid.append(list(line))
    return grid

def surrounding_count(grid: list[list[str]], i: int, j: int) -> int:
    surrounding_count = 0

    # TOP LEFT, TOP, TOP RIGHT
    if i > 0:
        if grid[i-1][j] == '@':
            surrounding_count += 1
        if j > 0:
            if grid[i-1][j-1] == '@':
                surrounding_count += 1
        if j < len(grid[0]) - 1:
            if grid[i-1][j+1] == '@':
                surrounding_count += 1

    # BOTTOM LEFT, BOTTOM, BOTTOM RIGHT
    if i < len(grid) - 1:
        if grid[i+1][j] == '@':
            surrounding_count += 1
        if j > 0:
            if grid[i+1][j-1] == '@':
                surrounding_count += 1
        if j < len(grid[0]) - 1:
            if grid[i+1][j+1] == '@':
                surrounding_count += 1

    # LEFT
    if j > 0:
        if grid[i][j-1] == '@':
            surrounding_count += 1

    # RIGHT
    if j < len(grid[0]) - 1:
        if grid[i][j+1] == '@':
            surrounding_count += 1
    
    return surrounding_count

def count_safe_cells(grid: list[list[str]]) -> int:
    safe_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '@':
                surrounding = surrounding_count(grid, i, j)
                if surrounding < 4:
                    safe_count += 1
    return safe_count

input = open('inputs/input.txt', 'r').read()
grid = build_grid(input)
print(count_safe_cells(grid))
