def format_input(input):
    input = input.split('\n')
    fresh_ranges = []
    ingredient_time = False
    ingredients = []

    for line in input:
        if line == '':
            ingredient_time = True
            continue
        elif not ingredient_time:
            fresh_ranges.append(list(map(int, line.split('-'))))
        else:
            ingredients.append(int(line))
    
    return fresh_ranges, ingredients

def find_clean_ranges(fresh_ranges: list[list[int, int]]) -> list[list[int, int]]:
    
    active_ranges = [fresh_ranges[0]]

    for start, end in fresh_ranges[1:]:
        if start <= active_ranges[-1][1]:
            active_ranges[-1][1] = max(active_ranges[-1][1], end)
        else:
            active_ranges.append([start, end])
    return active_ranges

def count_fresh_sum(clean_ranges: list[list[int, int]]) -> int:
    sorted_ranges = sorted(fresh_ranges, key=lambda x: x[0])
    clean_ranges = find_clean_ranges(sorted_ranges)
    clean_sum = 0
    for range_id in clean_ranges:
        clean_sum += range_id[1] - range_id[0] + 1
    return clean_sum

input = open('inputs/input.txt', 'r').read()
fresh_ranges, ingredients = format_input(input)


print(count_fresh_sum(fresh_ranges))