
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
            fresh_ranges.append(tuple(map(int, line.split('-'))))
        else:
            ingredients.append(int(line))
    
    return fresh_ranges, ingredients

def is_fresh(fresh_ranges: list[tuple[str, str]], ingredient: int) -> set[int]:
    for range_id in fresh_ranges:
        if range_id[0] <= ingredient <= range_id[1]:
            return True
    return False


def count_fresh_ingredients(ingredients: list[int], fresh_list: set[int]) -> int:
    count = 0
    for ingredient in ingredients:
        if is_fresh(fresh_ranges, ingredient):
            count += 1
    return count


input = open('inputs/input.txt', 'r').read()
fresh_ranges, ingredients = format_input(input)

print(count_fresh_ingredients(ingredients, fresh_ranges))