
### unlike part 1, part 2 actually makes use of the set...

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


def find_clean_ranges(fresh_ranges: list[list[int, int]]) -> list[tuple[int, int]]:
    active_ranges = []
    for range_id in fresh_ranges:
        overlap = False
        if not active_ranges:
            active_ranges.append(range_id)
            continue
        print(range_id)
        for active_range in active_ranges:
            # check each case. either it is within the range, or is on left overlap, or is on right overlap, or is bigger than range otherwise continue.

            # scenario 1: range_id is within the active_range
            if range_id[0] >= active_range[0] and range_id[1] <= active_range[1]:
                overlap = True
                print(f"scenario 1: range_id is within the active_range")
                break
            
            # scenario 2: range_id is on left overlap of active_range
            if range_id[0] < active_range[0] and range_id[1] >= active_range[0] and range_id[1] <= active_range[1]:
                active_range[0] = range_id[0]
                overlap = True
                print(f"scenario 2: range_id is on left overlap of active_range")
                break
            
            # scenario 3: range_id is on right overlap of active_range
            if range_id[0] >= active_range[0] and range_id[0] <= active_range[1] and range_id[1] > active_range[1]:
                active_range[1] = range_id[1]
                overlap = True
                print(f"scenario 3: range_id is on right overlap of active_range")
                break
            
            # scenario 4: range_id is superset of active range -- at this point I realized that I need to first sort the ranges by start, to avoid missing stuff.
            if range_id[0] < active_range[0] and range_id[1] > active_range[1]:
                active_range[0] = range_id[0]
                active_range[1] = range_id[1]
                overlap = True
                print(f"scenario 4: range_id is superset of active range")
                break

        
        if not overlap:
            active_ranges.append(range_id)
            print(f"scenario 5: range_id is not in any active range")
        
    return active_ranges

def sort_ranges(ranges: list[list[int, int]]) -> list[tuple[int, int]]:
    return sorted(ranges, key=lambda x: x[0])

input = open('inputs/input.txt', 'r').read()
fresh_ranges, ingredients = format_input(input)

sorted_ranges = sort_ranges(fresh_ranges)
print(sorted_ranges)
clean_ranges = find_clean_ranges(sorted_ranges)

print(clean_ranges)
clean_sum = 0
for range_id in clean_ranges:
    clean_sum += range_id[1] - range_id[0] + 1

print(clean_sum)


# print(count_fresh_ingredients(ingredients, fresh_ranges))


### basically add each range to a list. then when you add the next one, if there is a overlap,  either modify the existing range, or create a new one. modifying existing is probably easier.
### then iterate through the list and sum the differences between the start and end of each range.