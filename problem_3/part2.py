"""
This function checks if a new number makes the largest number larger.
    Args:
        number: The string of numbers
        digits: The number of digits to consider
    Returns:
        True if the new number makes the largest number larger and the digit to prune, False otherwise and 0 if no digit to prune
"""

def does_new_number_make_larger(number: list[str], test_digit: str, digits: int) -> (bool, int):

    diff = 0
    digit = 0

    curr_number = int(''.join(number))
    for i in range(digits):
        ## need to compare current number versus new number with current digit pruned. need to find the largest diff and only prune the bad digit for that.
        temp = number[:]
        temp.pop(i)
        temp.append(test_digit)
        temp = int(''.join(temp))
        if temp - curr_number > diff:
            digit = i
            diff = temp - curr_number
    
    return diff, digit


"""
This function finds the largest 12 digit number in a string of numbers, in forward facing order.
    Args:
        number: The string of numbers
    Returns:
        The largest 2 digit number
"""
def largest_joltage(number: str, digits: int) -> int:
    largest_number = list(number[0:digits])
    for i in range(digits, len(number)):
        larger, bad_digit = does_new_number_make_larger(largest_number, number[i], digits)
        if larger:
            largest_number.pop(bad_digit)
            largest_number.append(number[i])            
    largest_number = int(''.join(largest_number))
    return largest_number

"""
This function finds the total joltage of a list of battery packs.
    Args:
        numbers: The list of numbers
    Returns:
        The total joltage
"""
def total_joltage(numbers: list[str]) -> int:
    total_sum = 0
    for number in numbers:
        total_sum += largest_joltage(number, 12)
    return total_sum

input = open('inputs/input.txt', 'r').read()
input = input.split('\n')

print(total_joltage(input))