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
        smallest_digit = min(largest_number)
        if number[i] > smallest_digit:
            largest_number.pop(largest_number.index(smallest_digit))
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
        total_sum += largest_joltage(number, 2)
    return total_sum

input = open('inputs/input1.txt', 'r').read()
input = input.split('\n')

print(total_joltage(input))