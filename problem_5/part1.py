### input is a list of pairs of numbers, each pair is a range of numbers. then theres a blank line and then a list of numbers.
### we need to determine how many of the numbers in the second list are in any of the ranges in the first list.


### EDIT: This is an inefficient solution since the set operations are O(L) time complexity where L is the largest number in the list of ranges.

from typing import Any


input = open('inputs/input.txt', 'r').read()

def format_input(input):
    input = input.split('\n')
    ranges = []
    ingredient_time = False
    ingredients = []

    for line in input:
        if line == '':
            ingredient_time = True
            continue
        elif not ingredient_time:
            ranges.append(line.split('-'))
        else:
            ingredients.append(int(line))
    
    return ranges, ingredients


fresh_ranges, ingredients = format_input(input)

### want to make a set of the ranges, then for each ingredient, check if it is in any of the ranges

def fresh_list(fresh_ranges: list[tuple[str, str]]) -> set[int]:
    fresh_list = set()
    for range_id in fresh_ranges:
        items = list(range(int(range_id[0]), int(range_id[1]) + 1))
        fresh_list.update(items)
    return fresh_list



def count_fresh_ingredients(ingredients: list[int], fresh_list: set[int]) -> int:
    count = 0
    for ingredient in ingredients:
        if ingredient in fresh_list:
            count += 1
    return count

fresh_list = fresh_list(fresh_ranges)
print(count_fresh_ingredients(ingredients, fresh_list))