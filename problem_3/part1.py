"""
This function finds the largest 2 digit number in a string of numbers, in forward facing order.
    Args:
        number: The string of numbers
    Returns:
        The largest 2 digit number
"""
def largest_joltage(number: str) -> int:
    largest_number = 0
    for i in range(len(number) - 1):
        for j in range(i + 1, len(number)):
            if int(number[i]) * 10 + int(number[j]) > largest_number:
                largest_number = int(number[i]) * 10 + int(number[j])
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
        total_sum += largest_joltage(number)
    return total_sum

input = open('inputs/input.txt', 'r').read()
input = input.split('\n')

print(total_joltage(input))
