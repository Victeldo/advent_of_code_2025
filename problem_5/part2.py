
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
    active_ranges = []
    for range_id in fresh_ranges:
        overlap = False
        if not active_ranges:
            active_ranges.append(range_id)
            continue
        for active_range in active_ranges:
            if range_id[0] >= active_range[0] and range_id[1] <= active_range[1]:
                overlap = True
                break
            if range_id[0] >= active_range[0] and range_id[0] <= active_range[1] and range_id[1] > active_range[1]:
                active_range[1] = range_id[1]
                overlap = True
                break

        if not overlap:
            active_ranges.append(range_id)
        
    return active_ranges

input = open('inputs/input.txt', 'r').read()
fresh_ranges, ingredients = format_input(input)

sorted_ranges = sorted(fresh_ranges, key=lambda x: x[0])
clean_ranges = find_clean_ranges(sorted_ranges)

clean_sum = 0
for range_id in clean_ranges:
    clean_sum += range_id[1] - range_id[0] + 1

print(clean_sum)