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
                    grid[i][j] = '.'
    return safe_count

def total_removed_rolls(grid: list[list[str]]) -> int:
    total_rolls = 0
    while True:
        safe_count = count_safe_cells(grid)
        if not safe_count:
            break
        total_rolls += safe_count
    return total_rolls

input = open('inputs/input.txt', 'r').read()
grid = build_grid(input)
print(total_removed_rolls(grid))

## same thing as part 1 but now we gotta remove the rolls and then keep repeating until no more rolls can be removed. basically update to remove in place, and then keep repeating until no more count.